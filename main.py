import qrcode

url=input("Enter the URL or text to encode in QR Code: ").strip()
file_path="D:\\Files\\QRCode\\qrcode.png"
# Here "D:\\Files\\QRCode\\" is the file path and "qrcode.png" is the file name and format the generated qr code will be saved as.

qr=qrcode.QRCode()
qr.add_data(url)
img=qr.make_image()
img.save(file_path)

print(f"QR Code saved successfully at {file_path}")
