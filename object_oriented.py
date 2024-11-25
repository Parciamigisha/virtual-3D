'''object oriented'''
'''this will be the an object oriented version 
of the virtual game'''
import cv2


class facefinder:
	'''this is going to use haar cascade as filter to detect the largest face'''

	def __int__(self):
		print("face finder initialized")
		self.face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


	def find_face(slf, frame):
		'''returns face center(x,y), also draws a rect on face'''
		gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
		faces = self.face_cascade.detectMultiScale(gray, minNeighbors = 9)

		if faces is none:
			return none

		bx = by = bw = bh = 0 

		for (x, y, w, h) in faces:
		 	if w > bw :
		 		bx, by, bw, bh = x, y, w, h

		cv2.rectangle(gray, (bx, by), (bx+bw, by+bh), (0, 255, 255), 3)
		return(bx+bw/2),(by+bh/2)

'''------------------------------------------------------------'''
##main code
ff = facefinder()
print ('starting oo virtual3D')