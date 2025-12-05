import qrcode

url = input("Enter the URL to generate QR code: ")
qr = qrcode.QRCode()
qr.add_data(url)
# qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save("qrcode.png")
print("QR code generated and saved as qrcode.png") 
