"""
MKFC wordmark in the New Era 'split script' style:
  small "MOORABBIN" above a large "KANGAS" where each letter has a white
  outline, the top half of the letter interior is empty (cap colour shows
  through), and the bottom half is filled with a vertical gradient from
  white at the split line to light blue at the baseline.

Generates three variants:
  mkfc-wordmark-kangas.png                    - upright KANGAS
  mkfc-wordmark-kangas-italic.png             - KANGAS sheared right (~12.4°)
  mkfc-wordmark-kangas-italic-transparent.png - same on transparent background

Background colour is the canonical MKFC royal blue (#013087, Pantone 286 C).

Linux/WSL: the FONT paths below assume Open Sans is installed via
`sudo apt install fonts-open-sans`. On Windows, point FONT_MAIN/FONT_TOP at
a local copy of OpenSans-CondBold.ttf / OpenSans-Bold.ttf (or any bold
condensed sans you prefer).
"""
from PIL import Image, ImageDraw, ImageFont
from scipy.ndimage import binary_erosion
import numpy as np

ROYAL = (1, 48, 135)       # #013087 — Pantone 286 C
WHITE = (255, 255, 255)
LIGHT_BLUE = (200, 214, 240)  # #C8D6F0 — secondary palette

FONT_MAIN = "/usr/share/fonts/truetype/open-sans/OpenSans-CondBold.ttf"
FONT_TOP = "/usr/share/fonts/truetype/open-sans/OpenSans-Bold.ttf"

W, H = 2400, 1000
PAD = 80


def fit(text, max_w, max_h, path):
    lo, hi, best = 30, 1500, 30
    while lo <= hi:
        mid = (lo + hi) // 2
        f = ImageFont.truetype(path, mid)
        b = f.getbbox(text)
        if b[2] - b[0] <= max_w and b[3] - b[1] <= max_h:
            best, lo = mid, mid + 1
        else:
            hi = mid - 1
    return best


def build_main_layer(font, text, bbox, y_text_top, target_h, shear=0.0):
    """Render text with the split-script effect on a transparent layer.

    Returns (layer, outline_px). The text is rendered at the LEFT edge of
    the layer (x=0); the caller centres the layer on the canvas. Layer
    width = text_w + shear*text_h so the slanted top still fits.

    The upper half of each glyph interior is made transparent (cap colour
    shows through), and the lower half is filled with a vertical gradient
    from WHITE at the split line to LIGHT_BLUE at the bottom of the text.
    """
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    extra_w = int(abs(shear) * text_h) if shear else 0
    buf_w = text_w + extra_w + 4  # tiny safety margin

    layer = Image.new("RGBA", (buf_w, target_h), (0, 0, 0, 0))
    # Render so the bottom-left of glyphs sits at x = 0 (after shifting
    # away the font's own left side bearing), and the TOP of glyphs is
    # at y = y_text_top.
    ImageDraw.Draw(layer).text(
        (-bbox[0], y_text_top - bbox[1]), text, fill=WHITE, font=font
    )

    arr = np.array(layer)
    shape_mask = arr[..., 3] > 128
    outline_px = max(4, font.size // 32)
    interior = binary_erosion(shape_mask, iterations=outline_px)

    split_y = y_text_top + text_h // 2
    text_bottom = y_text_top + text_h

    ys = np.arange(target_h)[:, None].repeat(buf_w, axis=1)

    upper_interior = interior & (ys < split_y)
    arr[upper_interior] = [0, 0, 0, 0]

    lower_interior = interior & (ys >= split_y)
    if lower_interior.any():
        gradient_h = max(text_bottom - split_y, 1)
        t = np.clip((ys - split_y) / gradient_h, 0.0, 1.0)
        r_channel = (1 - t) * WHITE[0] + t * LIGHT_BLUE[0]
        g_channel = (1 - t) * WHITE[1] + t * LIGHT_BLUE[1]
        b_channel = (1 - t) * WHITE[2] + t * LIGHT_BLUE[2]
        arr[..., 0][lower_interior] = r_channel[lower_interior].astype(np.uint8)
        arr[..., 1][lower_interior] = g_channel[lower_interior].astype(np.uint8)
        arr[..., 2][lower_interior] = b_channel[lower_interior].astype(np.uint8)

    layer = Image.fromarray(arr)

    if shear:
        # AFFINE: OUTPUT(X,Y) -> INPUT(x = X + shear*Y - shear*H, y = Y).
        # Top of text (small Y) samples from small x -> top shifts right.
        a, b_aff, c = 1, shear, -shear * target_h
        layer = layer.transform(
            (buf_w, target_h),
            Image.AFFINE,
            (a, b_aff, c, 0, 1, 0),
            resample=Image.BICUBIC,
        )
    return layer, outline_px


def render(out_path, shear=0.0, transparent=False):
    if transparent:
        canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    else:
        canvas = Image.new("RGB", (W, H), ROYAL)

    top_text = "MOORABBIN"
    top_size = fit(top_text, int(W * 0.70), int(H * 0.18), FONT_TOP)
    top_font = ImageFont.truetype(FONT_TOP, top_size)
    b_top = top_font.getbbox(top_text)
    top_w, top_h = b_top[2] - b_top[0], b_top[3] - b_top[1]

    main_text = "KANGAS"
    main_h_max = int(H * 0.62)
    shear_budget = abs(shear) * main_h_max
    main_size = fit(
        main_text, W - 2 * PAD - int(shear_budget), main_h_max, FONT_MAIN
    )
    main_font = ImageFont.truetype(FONT_MAIN, main_size)
    b_main = main_font.getbbox(main_text)
    main_w, main_h = b_main[2] - b_main[0], b_main[3] - b_main[1]

    gap = int(H * 0.04)
    block_h = top_h + gap + main_h
    block_y = (H - block_h) // 2

    top_x = (W - top_w) // 2
    ImageDraw.Draw(canvas).text(
        (top_x, block_y - b_top[1]), top_text, fill=WHITE, font=top_font
    )

    main_y_top = block_y + top_h + gap
    main_layer, outline_px = build_main_layer(
        main_font, main_text, b_main, main_y_top, H, shear=shear
    )

    # Centre the (possibly slanted) layer horizontally.
    paste_x = (W - main_layer.width) // 2
    canvas.paste(main_layer, (paste_x, 0), main_layer)

    canvas.save(out_path + ".png", "PNG")
    if not transparent:
        canvas.save(out_path + ".jpg", "JPEG", quality=95)
    print(
        f"{out_path}: main {main_size}px, outline {outline_px}px, "
        f"top {top_size}px, shear {shear}, transparent {transparent}"
    )


render("mkfc-wordmark-kangas", shear=0.0)
render("mkfc-wordmark-kangas-italic", shear=0.22)  # ~12.4° lean
render("mkfc-wordmark-kangas-italic-transparent", shear=0.22, transparent=True)
