import sys
from pathlib import Path

# Add the function folder to the path for imports
sys.path.append(str(Path(__file__).parent.parent / "function"))

from lsb_extract import extract_message

def main():
    # Path to the input image
    image_path = str(Path(__file__).parent.parent / "assets" / "input_image.jpg")
    
    # Set the length of the hidden message in bytes (adjust as per your image)
    message_length = 10  # Example length

    # Extract message
    message_bytes = extract_message(image_path, message_length)
    message_text = message_bytes.decode('utf-8', errors='ignore')
    
    print("Extracted message:")
    print(message_text)

if __name__ == "__main__":
    main()
