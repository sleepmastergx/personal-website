# George Xue — Research Portfolio

A lightweight academic research website for George Xue, with a cobalt-and-paper field-notebook homepage. Fishing floats link to five fully visible research projects. The site is static HTML/CSS with a small optional script for motion controls and keyboard focus.

## Content

- Broad robot-learning interests, University of Toronto affiliation, and background
- Five research summaries and standalone detail pages
- Current submission statuses, ACDC acceptance and equal-contribution credit
- Researcher role for Preferenced Eureka at LEAF Lab
- An Actual Fishes section reserved for genuine fishing photos and stories

No fabricated catches, research outcomes, or placeholder photos are presented as real.

## Local preview and tests

Open `index.html`, or serve the repository root with a static server. Run:

```sh
python3 -m unittest discover -s tests -v
git diff --check
node --check assets/js/field-notes.js
```

Test the homepage and five project routes on desktop/mobile, project links, Back/Forward, keyboard focus, and Pause/Resume motion. Reduced-motion preferences disable animation automatically. Navigation and all research remain available without JavaScript.

## Files

- `index.html`: homepage and the fishing field notebook
- `assets/css/`: homepage styles
- `assets/js/field-notes.js`: optional motion toggle and focus behavior
- `assets/illustrations/`: original decorative artwork
- The current Shadow Hand animation is a looping GIF converted from the original Eureka project’s pen-spinning clip, with visible source credit, a pause control, and a still fallback for reduced-motion preferences. It is not presented as a Preferenced Eureka result.
- `assets/media/`: the previous, unused Farama reference clip and poster; its MIT license remains in `assets/licenses/`.
- `assets/licenses/MEDIA-SOURCES.md`: provenance and rights status for reference media.
- `projects/*/index.html`: complete research detail pages
- `css/styles.css`: research detail-page styles
- `images/*.webp`: existing manuscript figures
- `CNAME`: existing custom domain, preserved unchanged

## Deployment

GitHub Pages serves the repository root from `main` at https://georgexue.com. Keep `CNAME` unchanged. Keep status labels synchronized between the homepage and project pages. Confirm disclosure permission before adding unreleased manuscripts or results. Use only authorized imagery; add real fishing photos when supplied.

© George Xue. Research figure ownership remains with the respective authors.
