"""Dependency-free static-site regression checks. Run: python3 -m unittest discover -s tests -v."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import unittest

ROOT = Path(__file__).resolve().parents[1]
SLUGS = ('la-jepa', 'faster-wam', 'robot-memory', 'acdc', 'preferenced-eureka')


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.tags = []
        self.ids = []
        self.text = []
        self.anchor_depth = 0
        self.nested_anchors = False
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a':
            self.nested_anchors |= self.anchor_depth > 0
            self.anchor_depth += 1

    def handle_endtag(self, tag):
        if tag == 'a':
            self.anchor_depth -= 1

    def handle_data(self, data):
        self.text.append(data)

    def all(self, tag):
        return [attrs for name, attrs in self.tags if name == tag]

    @property
    def content(self):
        return ' '.join(' '.join(self.text).split())


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {path.resolve(): Page(path) for path in ROOT.rglob('*.html')}
        cls.home = cls.pages[(ROOT / 'index.html').resolve()]

    def test_all_five_projects_have_standalone_pages(self):
        self.assertEqual(len(self.pages), 6)
        for slug in SLUGS:
            self.assertIn((ROOT / 'projects' / slug / 'index.html').resolve(), self.pages)
            links = [a for a in self.home.all('a') if a.get('href') == f'projects/{slug}/']
            self.assertGreaterEqual(len(links), 2, slug)

    def test_local_links_assets_and_fragments_resolve(self):
        for path, page in self.pages.items():
            for tag, attrs in page.tags:
                for attr in ('href', 'src'):
                    if attr not in attrs:
                        continue
                    url = urlsplit(attrs[attr])
                    if url.scheme or url.netloc:
                        continue
                    target = (path.parent / unquote(url.path)).resolve() if url.path else path
                    if target.is_dir():
                        target /= 'index.html'
                    self.assertTrue(target.is_file(), f'{path.relative_to(ROOT)}: {attrs[attr]}')
                    if url.fragment and target in self.pages:
                        self.assertIn(unquote(url.fragment), self.pages[target].ids, f'{path}: {attrs[attr]}')

    def test_semantics_and_metadata(self):
        for path, page in self.pages.items():
            self.assertEqual(len(page.all('h1')), 1, path)
            self.assertEqual(len(page.all('main')), 1, path)
            self.assertEqual(len(page.ids), len(set(page.ids)), path)
            self.assertFalse(page.nested_anchors, path)
            self.assertEqual(page.anchor_depth, 0, path)
            self.assertTrue(page.all('title'), path)
            self.assertTrue(any(m.get('name') == 'description' for m in page.all('meta')), path)
            self.assertTrue(any(m.get('name') == 'viewport' for m in page.all('meta')), path)
            self.assertTrue(any(link.get('rel') == 'canonical' for link in page.all('link')), path)
            self.assertEqual(page.all('html')[0].get('lang'), 'en')
            for _, attrs in page.tags:
                for labelled_by in attrs.get('aria-labelledby', '').split():
                    self.assertIn(labelled_by, page.ids)
            for image in page.all('img'):
                self.assertTrue(image.get('alt'), path)
                self.assertGreater(int(image['width']), 0)
                self.assertGreater(int(image['height']), 0)

    def test_acdc_acceptance_and_other_statuses(self):
        accepted = 'CoRL 2026 Agentic Robotics Workshop · Accepted'
        self.assertIn(accepted, self.home.content)
        expected = {'acdc': accepted, 'la-jepa': 'ICLR 2027 · Under review',
                    'faster-wam': 'ICLR 2027 · Under review',
                    'robot-memory': 'CoRL 2026 Memory Workshop · Submitted'}
        for slug, status in expected.items():
            page = self.pages[(ROOT / 'projects' / slug / 'index.html').resolve()]
            self.assertIn(status, page.content)
            if slug != 'acdc':
                self.assertNotIn('Accepted', page.content)

    def test_research_interests_are_broader_than_project_list(self):
        self.assertIn('Research interests', self.home.content)
        self.assertIn('I’m broadly interested in robot learning', self.home.content)
        self.assertIn('My current projects explore several parts of this broader goal.', self.home.content)
        self.assertNotIn('My research focuses on embodied AI and world–action models', self.home.content)

    def test_expanded_project_descriptions(self):
        expected = {'la-jepa': 'two-frame observation', 'faster-wam': 'separate mixture of video layers',
                    'acdc': 'These visual decisions happen before flight.'}
        for slug, phrase in expected.items():
            page = self.pages[(ROOT / 'projects' / slug / 'index.html').resolve()]
            self.assertIn('motivation-heading', page.ids)
            self.assertIn(phrase, page.content)
            self.assertGreaterEqual(len(page.all('section')), 4)
        faster = self.pages[(ROOT / 'projects/faster-wam/index.html').resolve()]
        self.assertIn('not total task duration', faster.content)

    def test_leaf_research_assistant_background(self):
        self.assertIn('LEAF Lab', self.home.content)
        self.assertIn('Research Assistant', self.home.content)
        self.assertIn('University of Toronto Robotics Institute', self.home.content)

    def test_hobbies_and_honest_placeholder(self):
        self.assertIn('hobbies', self.home.ids)
        self.assertIn('Outside of research, I enjoy fishing.', self.home.content)
        placeholder = self.pages[(ROOT / 'projects/preferenced-eureka/index.html').resolve()]
        self.assertIn('Preferenced Eureka', placeholder.content)
        self.assertIn('This page is a placeholder', placeholder.content)
        self.assertIn('Details coming soon', placeholder.content)
        self.assertEqual(placeholder.all('img'), [])

    def test_public_resources_and_author_credit(self):
        acdc = self.pages[(ROOT / 'projects/acdc/index.html').resolve()]
        for page in (self.home, acdc):
            links = {a.get('href') for a in page.all('a')}
            self.assertIn('https://arxiv.org/abs/2509.16176', links)
            self.assertIn('https://acdc-drone.github.io/', links)
            self.assertIn('Equal-contributing author · Listed as George Z. Xue', page.content)
            for a in page.all('a'):
                if a.get('target') == '_blank':
                    self.assertIn('noopener', a.get('rel', ''))

    def test_detail_pages_keep_research_and_return_navigation(self):
        for slug in SLUGS:
            page = self.pages[(ROOT / 'projects' / slug / 'index.html').resolve()]
            self.assertTrue(any(a.get('href') == f'../../#{slug}' for a in page.all('a')))
            self.assertEqual(len([a for a in page.all('a') if a.get('aria-current') == 'page']), 1)
            if slug != 'preferenced-eureka':
                self.assertIn('Approach', page.content)
                self.assertIn('Scope', page.content)
                self.assertEqual(len(page.all('img')), 1)
                self.assertEqual(len(page.all('figcaption')), 1)

    def test_domain_and_dependency_free_behavior(self):
        self.assertEqual((ROOT / 'CNAME').read_text().strip(), 'georgexue.com')
        for page in self.pages.values():
            self.assertEqual(page.all('script'), [])


if __name__ == '__main__':
    unittest.main()
