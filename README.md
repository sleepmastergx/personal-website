# George Xue — Research Portfolio

A lightweight academic research website for George Xue, built with semantic HTML and responsive CSS. No build process, JavaScript, or external dependencies are required.

## Content

- Short biography and research interests
- Four research projects with manuscript figures, methods, results, and evaluation scope
- A fifth project, Preferenced Eureka, clearly marked as a placeholder
- Dedicated, shareable detail pages for every project
- A hobbies section featuring fishing
- Current submission labels, ACDC workshop acceptance, and public ACDC links
- Education, LEAF Lab research assistant experience, Huawei internship, confirmed email contact, and GitHub profile

The three under-review or submitted projects do not link to unreleased manuscripts. Project descriptions summarize collaborative work, rather than assigning unverified individual contributions. The ACDC equal-contribution credit follows the supplied manuscript.

## Local preview

Open `index.html` directly, or run a local static server from this directory:

```sh
python3 -m http.server 8000
```

Then open `http://localhost:8000`. All project cards open dedicated pages. Navigation works without JavaScript, including direct links and browser Back/Forward.

## Files

- `index.html`: homepage content, project cards, and hobbies
- `projects/*/index.html`: standalone project details, figures, and navigation
- `css/styles.css`: responsive layout, typography, accessibility, and print styles
- `images/*.webp`: optimized research figures from the project manuscripts
- `CNAME`: existing custom-domain configuration, preserved unchanged
- `tests/test_site.py`: dependency-free checks for internal links, content, metadata, and accessibility basics

## Tests

Run the static regression checks from the repository root:

```sh
python3 -m unittest discover -s tests -v
git diff --check
```

For visual QA, check the homepage and all five project routes on desktop and mobile, whole-card navigation, ACDC resource links, keyboard focus, and browser Back/Forward.

## Deployment

The site can be served directly from the repository root with GitHub Pages or another static host. Confirm the existing Pages branch and custom-domain settings before deploying. `CNAME` has not been changed by this redesign.

## Editing

Edit each project summary in `index.html` and its details in `projects/<slug>/index.html`. Keep status labels synchronized between the homepage and detail page. Preferenced Eureka is intentionally a placeholder until its details are ready. Keep each submission status current and confirm the disclosure permissions for unpublished work before deploying changes publicly. The confirmed contact address is `george.xue@robotics.utias.utoronto.ca`. Add a CV link only after confirming the intended file. When replacing figures, update the image dimensions, alt text, and figure credit together.

© George Xue. All rights reserved. Research figure ownership remains with the respective authors.
