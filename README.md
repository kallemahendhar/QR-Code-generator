.

📱 QR Code Generator

A simple and lightweight Python-based QR Code Generator that allows users to create QR codes for any URL. The QR code is generated as an image and saved locally for easy sharing or use in applications.

🚀 Features

✔️ Generates QR codes from any URL

✔️ Simple and beginner-friendly Python script

✔️ Saves QR code as a .png image

✔️ Works in any Python environment

🛠️ Technologies Used

Python

qrcode library (for creating QR codes)

Pillow (PIL) – automatically used by qrcode for image generation

📦 Installation

Make sure you have Python installed.

Install the required package:

pip install qrcode[pil]


Clone or download this project.

▶️ How to Run

Navigate to your project directory and run:

python App.py


You will be asked to enter:

The URL you want to convert into a QR code


A file named qrcode.png will be saved in your project folder.

📁 Project Structure
QR-Code-generator/
│── App.py
│── README.md
│── qrcode.png (generated after running)

📝 Code Explanation

The core logic of the project:

import qrcode

url = input("Enter the URL to generate QR code: ")
qr = qrcode.QRCode()
qr.add_data(url)
img = qr.make_image(fill='black', back_color='white')
img.save("qrcode.png")
print("QR code generated and saved as qrcode.png")


Takes user input

Creates a QR code object

Adds URL data

Generates an image with black-and-white theme

Saves it as qrcode.png
