import io
import time
import cv2
import numpy
import math
# from picamera.array import PiRGBArray
# from picamera import PiCamera

#Create an in-memory stream
# camera = PiCamera()

class Porta:
	def detect(frame):
		kernel = numpy.ones((5,5), numpy.uint8)		
		num_img=0
				
		#verde tarde
		#rangomax = numpy.array([60, 150, 100]) # B, G, R
		#rangomin = numpy.array([50, 80, 95])
		#verde dia
		rangomax = numpy.array([97, 255, 113]) # B, G, R
		rangomin = numpy.array([70, 100, 100])
		mask = cv2.inRange(frame, rangomin, rangomax)
		# reduce the noise
		opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

		box_x, box_y, box_width, box_height = cv2.boundingRect(opening)

		cv2.rectangle(frame, (box_x, box_y), (box_x+box_width, box_y+box_height), (0, 255, 0), 3)

		#amarelo
		rangomax2 = numpy.array([50, 130, 155]) # B, G, R
		rangomin2 = numpy.array([20, 80, 100])

		mask2 = cv2.inRange(frame, rangomin2, rangomax2)
		#reduce the noise
		opening2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel)

		x2, y2, w2, h2 = cv2.boundingRect(opening2)
		#print("Porta Detectada")
		#print(box_x, box_y, box_width, box_height)
		# cv2.rectangle(frame, (x2, y2), (x2+w2, y2 + h2), (0, 0, 255), 3)
		
		xc=box_x+(box_width/2)
		if xc==160:
			x=160
		else:
			x=160-xc

		yc=box_y+(box_height/2)
		if yc<120:
			y=120-yc
		elif yc>120:
			y=yc-120
		else:
			y=120

		angulo=math.degrees(math.atan(x/y))
		#print(angulo)	
		
		# cv2.imshow("teste", frame)
		# cv2.imwrite('teste'+str(num_img)+'.jpeg', frame)
		# num_img+=1

		# cv2.waitKey(0)
		
		
