# Story review — all 18 pages, 2026-07-05

Mechanical checks: all 22 external hotlinked images return 200; all internal links resolve; GA tag on every page; all pages regenerate cleanly from `generator/build.py`.

## Per-story status

| Story | Status | Notes |
|---|---|---|
| history | ✅ verified | 2014 founding, 2015 Maribago, 2016–2020 London, 2020 production house, post-ChatGPT pivot — all corroborated by bartsakwerda.com + ceb.wikipedia. **But see founding-year flag below.** |
| ai-filipino-llm | ✅ ok (positioning) | 180+ languages / 110M+ population claims are accurate. Roadmap framed as intent, not achievement. |
| ai-agents | ✅ ok (opinion) | Framed "move people up the stack" per policy. NEW: could link the BUDOTS AI Facebook post (open-source video-gen) as evidence. |
| drone-aerial | ✅ ok | Portfolio locations sourced from bartsakwerda.com. |
| maps | ✅ ok | 227 km POCC expedition claim matches Atlas Commune. NEW corroboration: Cebu 3D Map FB video, Trans-Central Highway / Pier 88 / Mandani Bay maps. |
| big-canoe | ✅ verified | 227 km, 123rd Independence Day, 5 days, SRP → Moalboal — matches atlascommune.com. |
| buzzy-budlong | ✅ verified | POCC founders (Budlong, Migalbin, Jimera) match Atlas Commune. |
| plank-g | 📝 draft | Still no public info found. Draft marker intact. |
| ironman | ✅ / ⚠ | 2024 race facts verified (1,385 athletes, 54 countries, Schoeman & Visser). 2022 Savoy section still unverified — but the 2026-01 YouTube short "Budots Media PH with Neviann Sanchez" now corroborates the Sanchez relationship. |
| brand-protection | ✅ policy holds | No name, no nationality — keep as is (defamation exposure). |
| olango-practice | ✅ verified | Matches Google Photos album + expedition timeline. |
| games-dev | ✅ verified | Summit facts (Feb 2024 Boracay, 300+/72/32; 2025 The Lind) verified at build time. |
| cinduy-wedding | 📝 draft → upgradable | **The wedding film is now public**: YouTube short o1zNuhSj92A, "Cindy Cinco Wedding 2026" (2026-04). Embed/link it and the draft marker can shrink. **Spelling flag:** page says "Cinduy", YouTube says "Cindy" Cinco — owner should confirm which is right. |
| lapulapu-projects | ✅ ok | JPARK/NUSTAR/LGU + Savoy/Camiguin long-haul paragraphs consistent with sources. |
| brides-of-triton | ✅ verified | "Annually since 2012" verified. Could add the Facebook video (cebu.lapu2/videos/1015805990550210). |
| dot7-eskrima-tour | 📝 draft | Eskrima/WEKAF facts verified; TudTud client + 2022 tour specifics still unverified. Draft marker intact. |
| community-initiatives | ✅ ok | Travel Company 2015 ✓, Chatbot meetup Dec 2017 ✓ (Medium corroborates). Japanese Meetup stated plainly as unverified. |
| dot-love-philippines | 📝 draft → upgradable | Campaign facts verified. **The DOT "Love Philippines" logo generator short (atCi9_hHIws, 2026-07) is now a concrete, linkable Budots deliverable** — can replace the draft placeholder. |

## Cross-cutting findings

1. **Founding-year discrepancy.** The archived budotsmediaph.com/about says "Budots Media, founded by Bart Sakwerda **in 2015**". Our site, bartsakwerda.com and Cebuano Wikipedia all say **2014** (post-Haiyan). Kept 2014 site-wide; owner should confirm (2015 may refer to the Maribago office move).
2. **Hero-image reuse.** Several stories share hero/card images (games-dev = ai-agents screenshot; dot7-eskrima = drone-aerial collage; cinduy = history beach photo). Cosmetic; replace as owner supplies photos.
3. **Hotlink risk remains for story heroes.** All 22 external images pass today, but Shopify/Google-Photos/Wix URLs can expire. budotsmediaph.com images are now local (`assets/img/budotsmediaph-com/`); heroes from webflow/shopify/bartsakwerda are the remaining pending item.
4. **Province map links still 404** (`provinces/<slug>.html` not built — 119 links in ph-provinces.svg).
5. **New material not yet in any story:** Foundever Sportsfests 2025/2026 (explicit capture credits), Green Concepts partnership (only on /projects and /showcase now), Asurion grand opening, ASEAN Tourism Showcase, Lechon Festival, Ascendion GCC launch. A "Corporate events" story could bundle these.
6. **budotsmedia.ph is a parked domain** (dotph registry parking, no content). budotsmediaph.com is NXDOMAIN (lapsed?) — content recovered from the 2025-06 Wayback snapshot and mirrored at /showcase/. Owner may want to renew/redirect these domains before the custom-domain move.
