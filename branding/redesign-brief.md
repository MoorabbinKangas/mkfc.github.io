---
layout: default
title: Logo redesign brief
permalink: /branding/redesign-brief/
description: "Designer brief for the MKFC logo redesign — split-script MOORABBIN / KANGAS wordmark, optimised for merchandise embroidery and print."
---

# Logo redesign brief

A brief for a freelance designer to deliver a refreshed MKFC logo system. Read the main [Branding](/branding/) guide first — palette, typography, and "don'ts" there are binding constraints, not suggestions.

## What we want

A single **horizontal wordmark** — for guernsey chest, cap fronts, polo embroidery, signage, hoodies. Wide aspect ratio (roughly 2:1 to 2.4:1).

This brief deliberately does **not** scope a separate square mark or monogram. Social media avatars will use a centred crop of the wordmark on royal blue; we accept that `MOORABBIN` / part of `KANGAS` will be the visible fragment at thumbnail size. A square companion mark may be commissioned in a future round once the wordmark is locked.

## Specification

The wordmark is a **New Era-style split-script lockup** with two lines of text. It draws directly on the North Melbourne FC wordmark family.

### Text content

- **Top line**: `MOORABBIN`
- **Bottom line**: `KANGAS` (note: not "KANGAROOS" — the supporter shortening)

### Type treatment

| Line | Treatment |
|---|---|
| `MOORABBIN` (top) | Bold condensed sans-serif caps, upright. Solid white fill. Roughly 30–35% of the bottom line's cap height. |
| `KANGAS` (bottom) | Bold condensed sans-serif **italic** caps. Letters are drawn as **outlined glyphs** (white outline ~4–6% of the cap height), with a **horizontal split at the letter mid-line**. Upper half: outline only, no fill (cap / garment colour shows through). Lower half: gradient fill, see below. |

Italic shear angle: roughly **12°** (matches the existing reference render at `/assets/merchandise/mkfc-cap-logo-split-italic.jpg`). The designer may tighten or relax this slightly for legibility but should not exceed ~15°.

### Gradient fill (lower half of `KANGAS`)

- **Colours**: `#FFFFFF` (White) at the top of the filled region, transitioning to `#C8D6F0` (Light Blue) at the bottom.
- **Direction**: vertical, top → bottom. The white edge sits at the split line; the light blue edge sits at the glyph baseline.
- **Per-letter, not across the word**: each letter carries its own copy of the gradient. The gradient does not span the whole word horizontally.
- **Smooth**, not banded. Designer should ensure the embroidery digitiser is briefed on how to approximate this with two adjacent fill colours if a true gradient stitch isn't available — see § Embroidery fallback below.

### Primary background

Royal Blue `#013087` (cap, guernsey). The white outline and the cap colour showing through the upper half are what create the contrast — **do not place the wordmark on a white background as the canonical version**; that's a derived variant.

### Reference render to evolve from

`/assets/merchandise/mkfc-cap-logo-split-italic.jpg` shows the split fill correctly but uses `KANGAROOS` and a solid white lower half (not a gradient). Use it for proportion and italic angle reference; the new direction supersedes it on text content and lower-half treatment.

### Designer latitude

Within the constraints above, the designer may:

- Adjust proportions, letter-spacing, outline weight, italic angle within stated limits.
- Propose a custom condensed letterform rather than off-the-shelf Open Sans Condensed Bold.
- Recommend (but not unilaterally adopt) a slight modification to the gradient stops if `#FFFFFF → #C8D6F0` proves too subtle at embroidery scale.

Hard constraints in the next section override anything in this section if they conflict.

### Embroidery fallback

A true thread gradient is not always available. Where the supplier cannot stitch a gradient, the designer must specify a **two-colour stepped approximation**: the top 60% of the filled region in white, the bottom 40% in light blue, with a single sharp transition. This approximation must be documented in the deliverable PDF as the "embroidery-safe" variant.

## Hard constraints

- **Palette is locked**: Royal Blue (Pantone 286 C / `#013087`), White, with Light Blue (`#C8D6F0`) permitted as an embroidery accent only. No navy, no teal, no gold, no black trims. See [Branding § Colour Palette](/branding/#colour-palette).
- **Three colours maximum** in any single rendition (royal blue + white + light blue). Embroiderers price per thread colour and detail past three colours stops reading at 60mm.
- **No gradients, no drop shadows, no bevels, no photographic effects.** Anything that can't be reproduced in flat embroidery thread or a single screen-print pass is out.
- **No combination with North Melbourne FC marks or wordmarks.** Our brand draws on the same family but is independent.
- **Reads at 60mm wide.** That's the cap-front minimum from the [Branding](/branding/) guide. If the wordmark needs detail to look correct at that size, it fails.
- **Typography** must align with the DIN / Helvetica Neue Condensed family (or a licensed equivalent the club can use without ongoing fees). Open Sans Condensed Bold is the current free fallback.

## Use-case requirements

### Guernsey (highest priority)

- Front-left chest, roughly hand-span sized (~150mm wide on adult kit).
- Royal blue garment → wordmark / mark in white + light blue accent. Reverse-colour version required.
- Screen-print and sublimation friendly: no halftones, strokes ≥ 1.5mm at production size.
- No back logo; back is reserved for player number + secondary sponsor.

### Cap (embroidered)

- Front panel ~60mm × 30mm, 2:1 aspect ratio. Horizontal wordmark is the primary use.
- All strokes ≥ 1.2mm at 60mm wide. Letter counter-shapes (the holes in `A`, `O`, `R`) must stay open after stitching.
- See [Cap design notes](/branding/cap-design/) for the existing colour-inversion approach on a royal blue cap.

### Polo / training tee

- Left chest embroidery, ~70–80mm wide. Same horizontal wordmark as the cap.
- Optional larger version on the back panel of jackets only.

### Social media avatar

- No separate square mark in this round (see § What we want).
- The avatar is a **centred 1:1 crop of the wordmark on royal blue** — the `MOORABBIN` / `KAN` fragment that lands inside the square is acceptable.
- Designer to supply a pre-cropped 1024×1024 PNG of this crop alongside the main wordmark exports, so the club doesn't have to re-crop the wide artwork itself.

## Deliverables

Supply all of the following, in a single zip:

### Vector source (mandatory)

- `.ai` and `.svg` for each of:
  - Horizontal wordmark, full colour (white outline + white→light-blue gradient, designed for royal blue background)
  - Horizontal wordmark, mono white (for use on royal blue where embroidery can't do the gradient — solid white fill in the lower half)
  - Horizontal wordmark, mono royal blue (for use on white — inverted colours, royal blue outline + royal-blue→mid-blue gradient)
  - Embroidery-safe variant of each of the above using the two-step fill approximation described in § Embroidery fallback.
- Fonts outlined / converted to paths. Do not assume the recipient has the typeface licensed.

### Raster exports

- PNG with transparent background at: 4000px (longest edge), 2000px, 1000px, 400px, 200px.
- JPG at 2000px (longest edge) on royal blue background — for use where transparency isn't supported.
- Avatar crop: 1024×1024 PNG, centred crop of the wordmark on royal blue.

### Documentation

- One-page PDF showing all variants with hex / Pantone callouts and a clear-space diagram.
- Embroidery digitising notes if any glyph or stroke needs special treatment at small sizes.

## File naming

Use the existing pattern in this repo so files drop straight into `/assets/`:

```
mkfc-wordmark-full.svg
mkfc-wordmark-white.svg
mkfc-wordmark-blue.svg
mkfc-wordmark-full-embroidery.svg
mkfc-wordmark-white-embroidery.svg
mkfc-wordmark-blue-embroidery.svg
mkfc-wordmark-avatar-1024.png
```

Raster exports follow the same stem with size suffixes, e.g. `mkfc-wordmark-full-2000.png`.

## Process & approvals

1. **Round 1 — direction**: a single wordmark refinement aligned to the § Specification above, supplied as a flat preview PDF or PNG. Show it on royal blue and on white. Include a mocked-up cap-front rendering at actual size (60mm × 30mm) so the committee can sanity-check legibility.
2. **Committee review**: the club committee approves the direction or sends a single round of feedback. Heritage / one-off variants need separate sign-off (per the [Branding](/branding/#dont) rules).
3. **Round 2 — refinement**: one round of revisions if needed.
4. **Final delivery**: full file set per § Deliverables above.

## Don't

- Don't add a tagline, founding year, or location string to the mark itself — those go in layout, not in the logo.
- Don't supply raster-only artwork. Embroiderers and printers need vector.
- Don't add extra colours "for the concept" with the intent to drop them later. Design within the three-colour ceiling from the start.
- Don't reuse the silver-bevelled shield from the legacy logo — it does not embroider and is being retired.

## Reference

- [Branding](/branding/) — canonical brand guide (palette, typography, logo rules).
- [Cap design notes](/branding/cap-design/) — working notes on cap embroidery, including the split-script approach.
- Legacy logo files (for reference only, not to copy): `/mkfc-logo-large.png`, `/mkfc-logo-large-no-text.png`.
- Split-script reference: `/assets/merchandise/mkfc-cap-logo-split-italic.jpg`.
