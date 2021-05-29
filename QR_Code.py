import  qrcode
import image
qr = qrcode.QRCode(
    version=1,
    box_size=6,
    border=3
)
qr.add_data("www.linkedin.com/in/chhandita-talapatra")
img=qr.make_image(back_color="blue")
img.save("LinkedIN.png")