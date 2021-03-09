import qrcode

web = "www.geeksforgeeks.org"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(web)
qr.make(fit=True)

img_qr = qr.make_image(fill_color="black",back_color="white")

#img_qr.save(prueba.png)

print(qr)