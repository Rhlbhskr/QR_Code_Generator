import qrcode

url=input("Enter the URL or text to encode in QR Code: ").strip()
file_path="D:\\Files\\QRCode\\qrcode.png"

qr=qrcode.QRCode()
qr.add_data(url)
img=qr.make_image()
img.save(file_path)

print(f"QR Code saved successfully at {file_path}")
