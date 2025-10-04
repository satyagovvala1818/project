QR Code Generator

This project is a simple Python program that generates QR codes for any kind of data such as URLs, text, phone numbers, or email addresses.
It uses the qrcode library to create the QR pattern and Pillow (PIL) to handle image creation and customization.

How It Works

The program encodes the given data into a QR code matrix, converts it into an image, and saves it as a PNG file.
You can also customize the QR code’s color, background, and filename.

Requirements

Install the required libraries:

pip install qrcode[pil] pillow

Usage

Run the file:

python qr_generator.py


Or use it in your code:

from qr_generator import generate_qr_code
generate_qr_code("https://www.google.com", "google_qr.png")

Summary

This project demonstrates how to generate and customize QR codes using Python, making it useful for learning and small automation tasks.
