import qrcode
from PIL import Image


def generate_qr_code(data, filename="qrcode.png", fill_color="black", back_color="white"):
    """
    Generate a QR code and save it as an image file.

    Args:
        data: The data to encode in the QR code (URL, text, etc.)
        filename: Output filename for the QR code image
        fill_color: Color of the QR code (default: black)
        back_color: Background color (default: white)
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)

    print(f"QR code generated successfully and saved as '{filename}'")
    return filename


if __name__ == "__main__":
    # Example usage
    data_to_encode = "https://www.example.com"

    # Generate basic QR code
    generate_qr_code(data_to_encode, "my_qrcode.png")

    # You can also customize colors
    # generate_qr_code(data_to_encode, "colored_qr.png", fill_color="blue", back_color="yellow")

    # Or encode different types of data
    # generate_qr_code("Hello, World!", "text_qr.png")
    # generate_qr_code("tel:+1234567890", "phone_qr.png")
    # generate_qr_code("mailto:example@email.com", "email_qr.png")
