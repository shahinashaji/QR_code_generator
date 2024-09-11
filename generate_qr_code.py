import qrcode
from qrcode.image.pil import PilImage

# Data to encode in the QR code as json
data = {
    "Language": "Python",
    "Website Reference": "https://www.python.org/"
}

# Data to encode in the QR code as a string
# data = "https://www.python.org/"

# Create a QR code instance
qrcode_instance = qrcode.QRCode(
    version=1,  # version determines the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # how much error correction the QR code should have
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border (in boxes)
)

# Add data to the QR code
qrcode_instance.add_data(data)
qrcode_instance.make(fit=True)

# Create an image of the QR code
# img = qr.make_image(fill='purple', back_color='white')

# Create an image with specific colors
img = qrcode_instance.make_image(fill_color='purple', back_color='white', image_factory=PilImage)

# Save the image to a file
img.save("qrcode_example.png")
