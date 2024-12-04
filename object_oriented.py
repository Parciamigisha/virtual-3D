'''object oriented'''
'''this will be the an object oriented version 
of the virtual game'''
import cv2
import numpy as nu

class facefinder:
	'''this is going to use haar cascade as filter to detect the largest face'''

	def __init__(self):
		print("face finder initialized")
		self.face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


	def find_face(self, frame):
		'''returns face center(x,y), also draws a rect on face'''
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = self.face_cascade.detectMultiScale(gray, minNeighbors = 9)

		if faces is None:
			return None

		bx = by = bw = bh = 0 

		for (x, y, w, h) in faces:
		 	if w > bw :
		 		bx, by, bw, bh = x, y, w, h

		cv2.rectangle(gray, (bx, by), (bx+bw, by+bh), (0, 255, 255), 3)
		return(bx+bw/2),(by+bh/2)

##class responsible for rendering
class Stage:
	#starts by initionling the display size, draws background grid bassed on position
	def __init__(self):
		self.disp_h = 0
		self.disp_w = 0
		self.cam_h = 720
		self.cam_w = 1280
		self.save_x = 960

	#a function that is going to get the position and size face
	def draw_target_xy(self, img, pos, size):
		cv2.circle(img, pos, size, (0,0,255), -1)
		cv2.circle(img, pos, int(size*.8),(255,255,255), -1)
		cv2.circle(img, pos, int(size*.6),(0,0,255), -1)
		cv2.circle(img, pos, int(size*.4),(255,255,255), -1)
		cv2.circle(img, pos, int(size*.2),(0,0,255), -1)

	#a fuction that is going to render the postion and size of the targets
	def draw_targetz(self,pos, facexy):
		tx,ty,tz = pos
		cv2.line(img,(ball0x, ball0y),50,(255,0,0), -1)
		cv2.line(img, (960+ int((600-960)*.3**2),540),(ball0x, ball0y),(255,0,0),3)
'''------------------------------------------------------------'''
##main code
ff = facefinder()
#get accesse to the web cap
cap = cv2.VideoCapture(cv2.CAP_ANY)
if not cap.isOpened():
	print("couldn't open web cam")
	exit()


while True:
	retval, frame = cap.read()
	if retval == False:
		print("camera error")

	ff.find_face(frame)
	cv2.imshow('q to quit', frame)

	if cv2.waitKey(30) == ord("q"):
		break



#destroys the cam
cap.release()

print ('starting oo virtual3D')