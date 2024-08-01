import qrcode

qr_img = qrcode.make("Hello World")

qr_img.save("qr_code_img.jpg")