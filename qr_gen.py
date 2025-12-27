# The QR CODE Generator by (PAPIAGAMERS)
#  You Can Use it by Just one Click To Run Command 
#      Easy To USE tHE qr Code
#        Let's Start To Make The QR Code Generator

import qrcode

# =========== QR CODE CONFIG =============

data = input('\nEnter The Text of URL : ').strip()
filename = input('\nEnter a FileName for The QRCode : ').strip()

# ========== QRCODE CONFIG MAKED =========

# ========== MAKE THE QR CODE ============
qr = qrcode.QRCode(box_size = 12, border = 5)
qr.add_data(data)

image = qr.make_image(fill_color = 'black', back_size = 'white')
image.save(filename) # This Can Save The File

# Printing The Value of QrCode:
print(f'\nQRCode is Saved in The: {filename}')
# ========= FINISHED NOW YOU CAN PLAY ======