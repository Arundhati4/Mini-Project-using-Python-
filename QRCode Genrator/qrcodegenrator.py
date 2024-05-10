import qrcode 
import image
qr = qrcode.QRCode(
    version = 15, 
    box_size = 10,
    border = 5
)

data = "https://www.youtube.com/channel/UCl6ic9RqdMimWlSCpkQ4ogw" 
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "Black", Back_color = "white")
img.save("test.png")