import qrcode 


def qr_code_generator():
	# qr code connection 
	qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
	)

	# Generating what data needs to be set in QR code
	qr.add_data('www.google.com')
	qr.make(fit=True)

	# making color to the QR Code
	img = qr.make_image(fill_color="black", back_color="white")
	# Saving the Generated QR Code in Local 
	img.save('qrcode.png')
	print(qr.data_list)

qr_code_generator()