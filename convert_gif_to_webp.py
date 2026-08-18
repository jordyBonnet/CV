"""Convertir des GIF animés en WebP animé (via Pillow).

Usage :
    python convert_gif_to_webp.py                 # convertit tous les .gif du dossier
    python convert_gif_to_webp.py Surfu2.gif      # convertit un fichier précis
    python convert_gif_to_webp.py --quality 85    # ajuste la qualité (0-100)

Le WebP animé est généralement bien plus léger qu'un GIF équivalent.
Les fichiers .gif d'origine sont conservés ; seuls des .webp sont créés à côté.
"""

import sys
from pathlib import Path

from PIL import Image, ImageSequence


def convert_gif_to_webp(gif_path: Path, quality: int = 80, method: int = 4) -> None:
    """Convertit un GIF animé en WebP animé en conservant durées et boucle."""
    gif = Image.open(gif_path)

    frames, durations = [], []
    for frame in ImageSequence.Iterator(gif):
        # RGBA pour préserver la transparence éventuelle du GIF.
        frames.append(frame.convert("RGBA"))
        durations.append(frame.info.get("duration", 100))

    webp_path = gif_path.with_suffix(".webp")
    frames[0].save(
        webp_path,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,          # boucle infinie, comme le GIF d'origine
        quality=quality,
        method=method,   # 0-6 : plus haut = meilleure compression (plus lent)
    )

    before_kb = gif_path.stat().st_size / 1024
    after_kb = webp_path.stat().st_size / 1024
    gain = (1 - after_kb / before_kb) * 100 if before_kb else 0
    print(f"{gif_path.name:30s} {before_kb:9.1f} Ko  ->  {after_kb:8.1f} Ko   (-{gain:.0f}%)")


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    quality = 80
    if "--quality" in sys.argv:
        idx = sys.argv.index("--quality")
        try:
            quality = int(sys.argv[idx + 1])
        except (IndexError, ValueError):
            print("Valeur --quality invalide, utilisation de 80.")

    base_dir = Path(__file__).parent
    if args:
        targets = [base_dir / a for a in args]
    else:
        targets = sorted(base_dir.glob("*.gif"))

    if not targets:
        print("Aucun fichier .gif trouvé.")
        return

    print(f"Conversion en WebP (qualité={quality}) :\n")
    for target in targets:
        if not target.exists():
            print(f"[ignoré] {target.name} introuvable")
            continue
        convert_gif_to_webp(target, quality=quality)

    print("\nTerminé. Pensez à remplacer les références .gif par .webp dans le HTML.")


if __name__ == "__main__":
    main()
