# Image Steganograph

A Python-based image steganography application that enables users to securely hide secret messages within digital images. The project uses image pixel manipulation techniques to embed text data into an image without causing noticeable visual changes.

## Overview

Image Steganography is the practice of concealing information inside digital media such that the existence of the hidden message remains undetected.

This project allows users to:

- Hide a secret message inside an image.
- Extract the hidden message from an encoded image.
- Preserve the visual appearance of the original image.
- Provide a simple and secure method of covert communication.

Unlike encryption, which protects the content of a message, steganography hides the existence of the message itself.

---

## Features

- Text Message Encoding
- Secret Message Extraction
- Image-Based Data Hiding
- Minimal Visual Distortion
- User-Friendly Interface
- Secure Information Sharing
- Fast Processing
- Support for Common Image Formats

---

## How It Works

1. The user selects an image.
2. A secret message is entered.
3. The application converts the message into binary data.
4. The binary data is embedded into the image pixels.
5. A new encoded image is generated.
6. The encoded image can later be decoded to reveal the hidden message.

---

## Applications

- Secure Communication
- Digital Watermarking
- Copyright Protection
- Data Authentication
- Confidential Information Sharing
- Cybersecurity Research
- Educational Demonstrations of Information Hiding

---

## Technology Stack

- Python
- OpenCV
- NumPy
- Pillow (PIL)
- Tkinter / Custom GUI (if applicable)

---

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd message
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

---

## Example

### Original Image

![Original Image](images/original.png)

### Encoded Image

![Encoded Image](images/encoded.png)

Although both images appear identical to the human eye, the encoded image contains a hidden message that can be extracted using the decoding process.

---

## Future Enhancements

- Password-Protected Encoding
- File Hiding Support
- AES Encryption Integration
- Multiple Image Format Support
- Web-Based Application
- Drag-and-Drop Interface

---

## Learning Outcomes

This project demonstrates concepts such as:

- Image Processing
- Data Encoding Techniques
- Information Security
- Digital Steganography
- Python Application Development
