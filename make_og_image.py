"""Génère og-image.jpg (1200x630) pour le partage social (Open Graph / Twitter).

Mise en page : photo à gauche (420px), panneau bleu avec texte à droite.

Usage :
    python make_og_image.py
"""

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
PHOTO_W = 420  # largeur du panneau photo
BLUE_DARK = (13, 59, 110)
BLUE_MID = (26, 95, 160)
BLUE_LIGHT = (220, 232, 247)
WHITE = (255, 255, 255)
MUTED = (154, 175, 200)

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "C:/Windows/Fonts"


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def crop_photo(path: str, box_w: int, box_h: int) -> Image.Image:
    """Recadre la photo (visage en haut) au ratio du panneau, centré horizontalement."""
    photo = Image.open(path)
    pw, ph = photo.size
    target_ratio = box_w / box_h
    if pw / ph > target_ratio:
        # photo trop large : on recadre la largeur
        new_w = int(ph * target_ratio)
        left = (pw - new_w) // 2
        photo = photo.crop((left, 0, left + new_w, ph))
    else:
        # photo trop haute : on garde le haut (visage)
        new_h = int(pw / target_ratio)
        photo = photo.crop((0, 0, pw, new_h))
    return photo.resize((box_w, box_h), Image.LANCZOS)


def main() -> None:
    img = Image.new("RGBA", (W, H), BLUE_DARK + (255,))
    d = ImageDraw.Draw(img)

    # ── Panneau photo (gauche) ─────────────────────
    photo = crop_photo(os.path.join(BASE, "jordy_bonnet.jpg"), PHOTO_W, H)
    img.paste(photo, (0, 0))

    # Liseré entre photo et panneau texte
    d.rectangle([PHOTO_W, 0, PHOTO_W + 6, H], fill=BLUE_MID)

    # ── Panneau texte (droite) ─────────────────────
    x = PHOTO_W + 70

    # Nom
    d.text((x, 140), "Jordy Bonnet", font=font("segoeuib.ttf", 80), fill=WHITE)

    # Ligne de séparation
    d.rectangle([x, 262, x + 110, 268], fill=BLUE_MID)

    # Tagline
    d.text((x, 305), "17 ans d\u2019innovation digitale en R&D", font=font("segoeui.ttf", 36), fill=BLUE_LIGHT)
    d.text((x, 368), "Data \u00b7 IA \u00b7 Robotique", font=font("seguisb.ttf", 34), fill=WHITE)
    d.text((x, 418), "Formulation & Chimie", font=font("seguisb.ttf", 34), fill=WHITE)

    # URL en bas
    d.text((x, 540), "jordybonnet.github.io/CV", font=font("segoeui.ttf", 26), fill=MUTED)

    out = os.path.join(BASE, "og-image.jpg")
    img.convert("RGB").save(out, "JPEG", quality=88, optimize=True)
    print(f"og-image.jpg : {W}x{H}, {os.path.getsize(out) / 1024:.1f} Ko")


if __name__ == "__main__":
    main()
