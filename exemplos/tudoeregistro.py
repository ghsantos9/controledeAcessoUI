# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import datetime
import imutils
import time
import cv2
import mysql.connector
from tkinter import tkinter.messagebox

mydb = mysql.connector.connect(host="192.168.1.145",user="test",passwd="cerejinha123",database="cadastro")

mycursor = mydb.cursor()


# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=2).start()
#vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
# open the output CSV file for writing and initialize the set of
# barcodes found thus far

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it to
	# have a maximum width of 400 pixels
	frame = vs.read()
	#frame = imutils.resize(frame, width=600)
	# find the barcodes in the frame and decode each of the barcodes
	barcodes = pyzbar.decode(frame)

	# loop over the detected barcodes
	for barcode in barcodes:
		# extract the bounding box location of the barcode and draw
		# the bounding box surrounding the barcode on the image
		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

		# the barcode data is a bytes object so if we want to draw it
		# on our output image we need to convert it to a string first
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type

		# draw the barcode data and barcode type on the image
		text = "{} ({})".format(barcodeData, barcodeType)

		#print(barcodeData) # esse é o que tem no qrcode

		cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
		# if the barcode text is currently not in our CSV file, write
		# the timestamp + barcode to disk and update the set
		

		separar=barcodeData.split("\r\n")  #TESTE3\r\n1\r\n1  rg=9 numeros ra=13 numeros
		print("Separando "+str(separar))
		
		try:
			nome=separar[0]
			rg=str(separar[1])
			ra=str(separar[2])
			comando="select nome from pessoas where rg='{}' and ra='{}'".format(rg,ra)

			mycursor.execute(comando)
            
			myresult = mycursor.fetchall()

			
			if str(myresult) == "[]":
				print("nao cadastrado, tentando cadastrar")
                
			else:
				print("Bem Vindo {}".format(str(myresult).replace("[('","").replace("',)]","")))


		except:
			print("formato invalido")


	# show the output frame
	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()
