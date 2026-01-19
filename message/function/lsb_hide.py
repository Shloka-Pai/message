from PIL import Image

def bytes_to_binary(data: bytes) -> str:
    """Convert bytes to a binary string."""
    return ''.join(format(byte, '08b') for byte in data)

def hide_message(image_path: str, output_path: str, message_bytes: bytes):
    """
    Hide a compressed message in an image using LSB steganography.

    :param image_path: Path to the input image
    :param output_path: Path to save the output image
    :param message_bytes: Compressed message as bytes
    """
    # Convert message to binary
    binary_msg = bytes_to_binary(message_bytes)
    
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size
    idx = 0

    for y in range(height):
        for x in range(width):
            if idx < len(binary_msg):
                r, g, b = pixels[x, y]

                # Replace LSB of Red, Green, Blue with message bits
                r = (r & ~1) | int(binary_msg[idx]) if idx < len(binary_msg) else r
                idx += 1
                g = (g & ~1) | int(binary_msg[idx]) if idx < len(binary_msg) else g
                idx += 1
                b = (b & ~1) | int(binary_msg[idx]) if idx < len(binary_msg) else b
                idx += 1

                pixels[x, y] = (r, g, b)
            else:
                break

    img.save(output_path)
    print(f"Message hidden successfully in {output_path}")
