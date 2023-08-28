import segno
data_image = "https://www.linkedin.com/in/tor-tar-40814398/"
qrcode = segno.make(data_image)
qrcode.save('qrcode_emmanuel.png',dark='darkred', light='lightblue', scale=10)