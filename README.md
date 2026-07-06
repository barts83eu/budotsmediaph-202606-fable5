# Budots Media Philippines — Portfolio Website

**Live site:** https://barts83eu.github.io/budotsmediaph-202606-fable5/

Portfolio and company website for **Budots Media / Budots Media Philippines**, a Lapu-Lapu City–based media production house founded in 2014 by Bart Sakwerda, with sister entities in Poland (Budots Media Poland) and London (Budots Media London). The site presents the company's mission, history, client portfolio, and a collection of story pages covering its work — from drone and aerial surveys, event coverage (Ironman 70.3 Lapu-Lapu, Brides at Triton wedding expo), and Department of Tourism campaigns, to its current priority: development of a sovereign Filipino language model and multimodal generative AI.

## About the website

A fully static site — no framework, no build dependencies for the pages themselves. Design follows the company brief:

- Black-to-white top-to-bottom gradient with parallax scrolling layers
- Canvas particle system that fades as the page scrolls into the white zone
- Scroll indicators: top progress bar, hero mouse-wheel icon, right-side section dots
- Bebas Neue display type (free stand-in for Bebas Neue Pro, which is used when installed)
- Mobile-first: `svh` units, `clamp()` typography, auto-fit card grids
- Clickable SVG map of all 119 Philippine provinces (`assets/img/ph-provinces.svg`)
- Client logo wall with 35+ localized logos (DOT, BYD, JPARK, NUSTAR, Megaworld, Accenture, JPMorganChase, Harley-Davidson, and more)

## Repository layout

```
website/       The publishable site (this folder is what gets deployed)
generator/     Story-page generator: build.py + template.html → website/stories/<slug>/index.html
instructions/  Content sources, build notes, and asset references (not deployed)
```

To add or edit a story page: add/modify a `PAGES` entry in [generator/build.py](generator/build.py) and run `python3 generator/build.py`. To preview locally, open [website/index.html](website/index.html) in a browser.

## Site map

Machine-readable: [website/sitemap.xml](website/sitemap.xml) (26 URLs, referenced from [website/robots.txt](website/robots.txt)).

```
/  Homepage — parallax one-pager
├── #mission      Mission
├── #history      Company history timeline
├── #portfolio    Clients & logo wall
├── #stories      Story cards (link to the pages below)
├── #assets       Philippines province map (clickable SVG)
├── #genai        Generative AI work
├── #three-d      3D / AR / VR & photogrammetry
├── #contact      Contact & social links
│
└── stories/                         One folder per story; old flat .html URLs redirect
    ├── history/                     Our History (2014 founding → today)
    ├── lapulapu-projects/           Projects in Lapu-Lapu City
    ├── drone-aerial/                Drones & Aerial Surveys
    ├── maps/                        Philippines in Maps
    ├── ai-filipino-llm/             A Sovereign Filipino Language Model
    ├── ai-agents/                   AI Agents in the Edit Bay
    ├── dot-love-philippines/        DOT — Love the Philippines campaign
    ├── dot7-eskrima-tour/           The DOT7 Eskrima Tour of Cebu
    ├── ironman/                     Ironman Philippines (IM 70.3 Lapu-Lapu 2024 + Savoy 2022)
    ├── brides-of-triton/            Brides at Triton wedding expo (JPARK)
    ├── big-canoe/                   Big Canoe, Bigger Dream (OC6 paddling)
    ├── buzzy-budlong/               Buzzy Budlong
    ├── olango-practice/             Practice at Olango
    ├── cleevan-alegres/             Cleevan Alegres — The Little Merman
    ├── dream-keeper/                The Sinking of M/V Dream Keeper (hand-authored parallax page + own assets/)
    ├── games-dev/                   Game Development in the Philippines
    ├── community-initiatives/       Bart Sakwerda's community initiatives
    ├── brand-protection/            Defending a Brand
    ├── plank-g/                     Mary Grace — Plank G (draft)
    └── cinduy-wedding/              The Cinduy Cinco Wedding (draft)
```

Note: the province map links to `provinces/<slug>.html` pages that are not built yet; pages marked *(draft)* carry visible draft markers awaiting owner-supplied facts (see [instructions/build-notes-reference.md](instructions/build-notes-reference.md)).

## Deployment

Deployed to **GitHub Pages** via GitHub Actions ([.github/workflows/pages.yml](.github/workflows/pages.yml)): every push to `main` publishes the `website/` folder. No build step — the folder is uploaded as-is.

---

*Site built with Anthropic Claude (Fable 5), 2026-06/07.*
