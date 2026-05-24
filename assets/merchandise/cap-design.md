---
layout: default
title: Cap design notes
permalink: /branding/cap-design/
description: "Working notes on translating the MKFC mark to embroidered caps."
---

# Cap design notes

Working notes for translating the MKFC mark onto a **royal blue cap** (royal blue `#013087`, Pantone 286 C). Supplements the main [Branding](/branding/) guide — refer there for the canonical palette, typography, and logo rules.

## Colour roles on a royal blue cap

The cap supplies the royal blue background; the wordmark adds white and light blue on top. Three colours total — the right ceiling for clean embroidery.

| Element | Colour |
|---|---|
| Cap body | Royal Blue `#013087` (Pantone 286 C) |
| `MOORABBIN` (top line) | White, solid fill |
| `KANGAS` outline | White |
| `KANGAS` upper-half interior | Cap royal blue showing through (no thread) |
| `KANGAS` lower-half interior | Gradient: white at the split line → light blue `#C8D6F0` at the baseline |

True thread gradients aren't universally supported. If the embroiderer can't stitch a gradient, fall back to a **two-step approximation**: the top 60% of the filled region in white, the bottom 40% in light blue, single hard transition. Document which version was used so re-orders match.

## Layout and proportions

- Cap front panel target is roughly **4.5″ × 2.25″ (60mm × 30mm)** — about a **2:1 to 2.4:1** aspect ratio. Design the artwork to that horizontal ratio rather than the square brand mark.
- The brand guide minimum embroidery width is **60mm**; do not go smaller.
- **Canonical layout — split-script wordmark**: small "MOORABBIN" above large "KANGAS" in bold condensed italic. White outline; upper half of letters is outline-only (cap colour shows through); lower half is filled with a vertical gradient from **white at the split line** to **light blue `#C8D6F0` at the baseline**. No crest, no kangaroo silhouette. This is the locked direction — see the [Logo redesign brief](/branding/redesign-brief/) for the full spec.
- **Legacy layout — crest left + two-line wordmark** (`mkfc-cap-logo.png`): the kangaroo+shield on the left with "MOORABBIN KANGAROOS" on the right. Kept for reference only; the bevelled shield is being retired and should not be used on new cap orders.
- For very small placements (cap side, strap), use the `MOORABBIN` line alone — do not isolate the kangaroo silhouette from the legacy crest.

## Supplying artwork to the embroiderer

- **Always provide a vector file** (SVG, AI, or EPS) where possible. Embroiderers digitise from vectors; raster (PNG/JPG) forces them to trace and introduces drift.
- If only raster is available, supply at **300 dpi or higher** at the final stitched size.
- Specify thread colours by Pantone where the supplier supports it: royal blue = **Pantone 286 C**, light blue = closest match to `#C8D6F0`, white = pure `#FFFFFF`. Madeira / Robison-Anton equivalents are acceptable.
- Embroidery cannot reproduce gradients, drop shadows, or the silver shield bevel — flatten these out before sending.
- Letter strokes and outlines below ~1.2mm at final size will not stitch cleanly. Keep outlines bold.

## Don't

- Don't keep the original blue-on-white colour scheme on a royal blue cap — the brand blue is too close to the cap colour and the mark disappears.
- Don't add a coloured "patch" background behind the logo that breaks the cap colour. The cap *is* the background.
- Don't introduce off-palette blues (navy, teal, sky) when matching threads; stick to the documented royal, mid, and light blues from the [Branding](/branding/) guide.

## Reference files

Generated cap-ready artwork (in `/assets/merchandise/`):

- `mkfc-wordmark-kangas-italic.png` / `.jpg` — **canonical** split-script wordmark, italic `KANGAS` with white→light-blue gradient lower half, on royal blue.
- `mkfc-wordmark-kangas-italic-transparent.png` — same wordmark on transparent background, for compositing.
- `mkfc-wordmark-kangas.png` / `.jpg` — upright variant (no italic shear). The italic version is the canonical direction.
- `mkfc-cap-logo-split-italic.jpg` / `.png` — **superseded** legacy reference; uses `KANGAROOS` and a solid white lower half (no gradient).
- `mkfc-cap-logo.png` / `.jpg` — legacy crest-left + two-line wordmark. Reference only; bevelled shield is retired.

Generator script: `assets/merchandise/make_cap_logo_split.py` produces the canonical wordmark files above. Edit the constants at the top (`ROYAL`, `LIGHT_BLUE`, font paths) and re-run with `python3 make_cap_logo_split.py`. Requires Pillow, numpy, and scipy.
