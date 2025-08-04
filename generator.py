import os
import random

from PIL import Image, ImageDraw, ImageFont


def generate_decoder_image(
    text: str, width: int = 800, height: int = 400, font_size: int = 80, alpha: int = 10
):
    """Generates decoder image with hidden text which is only visible with red decoder glasses.

    Args:
        text (str): Text that should be hidden in image.
        width (int, optional): Width of the image. Defaults to 800.
        height (int, optional): Height of the image. Defaults to 400.
        font_size (int, optional): Font size of hidden text. Defaults to 80.
        alpha (int, optional): Controls opacity of hidden text. Defaults to 10.

    Returns:
        Generated image with hidden text.
    """
    # 1️⃣ Generate Red-Yellow-Orange-Pink Noise
    img = Image.new("RGB", (width, height), "white")
    pixels = img.load()

    colors = [
        (255, 50, 50),  # Red
        (255, 255, 255),  # White
        (255, 200, 0),  # Yellow
        (255, 120, 0),  # Orange
        (255, 50, 150),  # Pink
    ]
    weights = [0.4, 0.2, 0.15, 0.15, 0.1]  # Probability for each color

    for y in range(height):
        for x in range(width):
            pixels[x, y] = random.choices(colors, weights=weights, k=1)[0]

    # 2️⃣ Opaque cyan text
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    font_path = os.path.join(os.path.dirname(__file__), "fonts", "arial.ttf")
    font = ImageFont.truetype(font_path, size=font_size)

    bbox = draw.textbbox((0, 0), text, font=font)
    text_x = (width - (bbox[2] - bbox[0])) // 2
    text_y = (height - (bbox[3] - bbox[1])) // 2

    draw.text((text_x, text_y), text, font=font, fill=(0, 180, 180, alpha))

    # 3️⃣ Combine layers
    combined = Image.alpha_composite(img.convert("RGBA"), overlay)

    return combined
