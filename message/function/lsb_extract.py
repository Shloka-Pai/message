from PIL import Image

def binary_to_bytes(binary_msg: str) -> bytes:
    """Convert a binary string to bytes."""
    byte_list = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    return bytes([int(b, 2) for b in byte_list])

def extract_message(image_path: str, message_length: int) -> bytes:
    """
    Extract a hidden message from an image using LSB steganography.

    :param image_path: Path to the image with hidden message
    :param message_length: Length of the message in bytes
    :return: Extracted message in bytes
    """
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    width, height = img.size

    idx = 0
    binary_msg = ""

    for y in range(height):
        for x in range(width):
            if idx >= message_length * 8:
                break
            r, g, b = pixels[x, y]
            for color in (r, g, b):
                if idx < message_length * 8:
                    binary_msg += str(color & 1)
                    idx += 1
        if idx >= message_length * 8:
            break

    return binary_to_bytes(binary_msg)
