"""CV download regression checks."""
from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.links.append(dict(attrs))


class CVTests(unittest.TestCase):
    def test_homepage_links_to_readable_pdf(self):
        page = Links()
        page.feed((ROOT / 'index.html').read_text())
        links = [a for a in page.links if a.get('href') == 'files/George_Xue_CV.pdf']
        self.assertEqual(len(links), 3)
        self.assertTrue(all(a.get('type') == 'application/pdf' for a in links))
        self.assertEqual(links[0].get('aria-label'), 'View CV (PDF)')
        pdf = ROOT / links[0]['href']
        self.assertTrue(pdf.read_bytes().startswith(b'%PDF-'))
        self.assertGreater(pdf.stat().st_size, 1000)

    def test_cv_has_a_prominent_hero_link(self):
        html = (ROOT / 'index.html').read_text()
        page = Links()
        page.feed(html)
        hero = [a for a in page.links if a.get('class') == 'hero-cv']
        self.assertEqual(len(hero), 1)
        self.assertEqual(hero[0]['href'], 'files/George_Xue_CV.pdf')
        self.assertEqual(hero[0]['aria-label'], 'View CV (PDF)')
        self.assertLess(html.index('class="hero-cv"'), html.index('class="angler-notebook"'))
        self.assertIn('<span>View CV</span><span class="cv-format">PDF</span>', html)
        css = (ROOT / 'assets/css/field-notes.css').read_text()
        self.assertIn('.v2 .hero-cv:focus-visible', css)
        self.assertIn('min-height:48px', css)


if __name__ == '__main__':
    unittest.main()
