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

	#a function that redraws all the tunal and the targets 
	def update(self, facexy):
		x,y = facexy
		e = .9 #for smoothing constantly
		x = e * x + (1-e)*self.save_x
		self.save_x = x
		img = np.zeros([1080, 1920, 3])
		decay = .3
		sx = sy = 0
		dx = int((x - self.com_w/2)*2)
		for i in range(1,7):
			sx = sx + int((960-sx)*decay)
			sy = sy + int((540-sy)*decay)
			dx = int(dx * decay)
			#print(sx,sy)
			cv2.rectangle(img, (sx+dx,sy),(1920-sx+dx, 1080-sy),(255,255,255),1)

			ball0x = 600+int((x - self.com_w/2)*2*.6)
			ball0y = 540

			cv2.line(img, (960+ int((600-960)*.3**2),540),(ball0x, ball0y),(255,0,0),3)
			self.draw_target_xy(img, (ball0x,ball0x),35)

			ball1x = 1000 + int((x - self.com_w/2)*2*.2)
			ball1y = 440

			cv2.line(img, (960+ int((1200-960)*.3**2), 540 - int((540 - 340)*.3**2)),(ball1x, ball1y)(255,0,0),3)
			self.draw_target_xy(img, (ball1x, ball1y), 25)

			ball2x = 1100 + int((x - self.com_w/2)*2*.9)
			ball2y = 650

			cv2.line(img, (960+int((1100-960)*.3**2),540 - int((540-650)*.3**2)),(ball2x, ball2y), (255, 0, 0),3)
			self.draw_target_xy(img, (ball2x, ball2y),50)

			cv2,imshow("parcia's Game" ,img)
'''----------------------------------------------------------------------------------------------------------------------'''
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