# George Xue — Research Portfolio

A lightweight academic research website for George Xue, built with semantic HTML and responsive CSS. No build process, JavaScript, or external dependencies are required.

## Content

- Short biography and research interests
- Four research projects with manuscript figures, methods, results, and evaluation scope
- Accurate submission labels and public ACDC links
- Education, research internship, confirmed email contact, and GitHub profile

The three under-review or submitted projects do not link to unreleased manuscripts. Project descriptions summarize collaborative work, rather than assigning unverified individual contributions. The ACDC equal-contribution credit follows the supplied manuscript.

## Local preview

Open `index.html` directly, or run a local static server from this directory:

```sh
python3 -m http.server 8000
```

Then open `http://localhost:8000`. Navigation and project-detail disclosure controls work without JavaScript.

## Files

- `index.html`: content, metadata, and semantic structure
- `css/styles.css`: responsive layout, typography, accessibility, and print styles
- `images/*.webp`: optimized research figures from the project manuscripts
- `CNAME`: existing custom-domain configuration, preserved unchanged

## Deployment

The site can be served directly from the repository root with GitHub Pages or another static host. Confirm the existing Pages branch and custom-domain settings before deploying. `CNAME` has not been changed by this redesign.

## Editing

Edit the project entries directly in `index.html`. Keep each submission status current and confirm the disclosure permissions for unpublished work before deploying changes publicly. The confirmed contact address is `george.xue@robotics.utias.utoronto.ca`. Add a CV link only after confirming the intended file. When replacing figures, update the image dimensions, alt text, and figure credit together.

© George Xue. All rights reserved. Research figure ownership remains with the respective authors.
