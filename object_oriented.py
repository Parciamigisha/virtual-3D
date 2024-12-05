'''object oriented'''
'''this will be the an object oriented version 
of the virtual game'''
import cv2
import numpy as np

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
    # Initialize the display and camera parameters
    def __init__(self):
        self.disp_h = 0
        self.disp_w = 0
        self.cam_h = 720
        self.cam_w = 1280
        self.save_x = 960  # To smooth horizontal movement
        self.save_y = 540  # To smooth vertical movement

    # A function to draw target circles
    def draw_target_xy(self, img, pos, size):
        cv2.circle(img, pos, size, (0, 0, 255), -1)
        cv2.circle(img, pos, int(size * 0.8), (255, 255, 255), -1)
        cv2.circle(img, pos, int(size * 0.6), (0, 0, 255), -1)
        cv2.circle(img, pos, int(size * 0.4), (255, 255, 255), -1)
        cv2.circle(img, pos, int(size * 0.2), (0, 0, 255), -1)

    # Update method to handle rendering based on face position
    def update(self, facexy):
        x, y = facexy
        e = 0.9  # Smoothing factor

        # Smooth the x and y positions
        x = e * x + (1 - e) * self.save_x
        y = e * y + (1 - e) * self.save_y

        # Save the smoothed positions
        self.save_x = x
        self.save_y = y

        # Create a blank image
        img = np.zeros([1080, 1920, 3], dtype=np.uint8)

        decay = 0.3
        sx = sy = 0
        dx = int((x - self.cam_w / 2) * 2)
        dy = int((y - self.cam_h / 2) * 2)  # Vertical offset based on smoothed y

        for i in range(1, 7):
            # Adjust the shrinking rectangle dimensions with decay
            sx = sx + int((960 - sx) * decay)
            sy = sy + int((540 - sy) * decay)
            dx = int(dx * decay)
            dy = int(dy * decay)

            # Draw shrinking rectangles
            cv2.rectangle(img, (sx + dx, sy + dy), (1920 - sx + dx, 1080 - sy + dy), (255, 255, 255), 1)

        # Draw targets and lines based on the smoothed x and y
        ball0x = 600 + int((x - self.cam_w / 2) * 0.6)
        ball0y = 540 + int((y - self.cam_h / 2) * 0.6)
        cv2.line(img, (960 + int((600 - 960) * 0.3**2), 540), (ball0x, ball0y), (255, 0, 0), 3)
        self.draw_target_xy(img, (ball0x, ball0y), 35)

        ball1x = 1000 + int((x - self.cam_w / 2) * 0.2)
        ball1y = 440 + int((y - self.cam_h / 2) * 0.2)
        cv2.line(img, (960 + int((1200 - 960) * 0.3**2), 540 - int((540 - 340) * 0.3**2)), (ball1x, ball1y), (255, 0, 0), 3)
        self.draw_target_xy(img, (ball1x, ball1y), 25)

        ball2x = 1100 + int((x - self.cam_w / 2) * 0.9)
        ball2y = 650 + int((y - self.cam_h / 2) * 0.9)
        cv2.line(img, (960 + int((1100 - 960) * 0.3**2), 540 - int((540 - 650) * 0.3**2)), (ball2x, ball2y), (255, 0, 0), 3)
        self.draw_target_xy(img, (ball2x, ball2y), 50)

        # Show the image in a window
        cv2.imshow("Parcia's Game: q to EXIT", img)

'''----------------------------------------------------------------------------------------------------------------------'''
##main code
ff = facefinder()
stage = Stage()
img = np.zeros([1080,1920,3])
#cv2.imshow("parcia's Game", img)
#get accesse to the web cap
cap = cv2.VideoCapture(cv2.CAP_ANY)
if not cap.isOpened():
	print("couldn't open web cam")
	exit()

moved = False

while True:
	#reads the frame
	ret, frame = cap.read()
	#if frame is read correctly ret is true
	if not ret:
		print("error reading frame. Exiting.....")

	facexy = ff.find_face(frame)
	frame_small = cv2.resize(frame, (frame.shape[1]//4, frame.shape[0]//4), interpolation = cv2.INTER_LINEAR)
	cv2.imshow('q to quit', frame_small)

	if not moved:
		cv2.moveWindow('q to quit', 1080,0)
		moved = True
	if facexy is not None:
		img = stage.update(facexy)

	#stops the game if q is pressed
	if cv2.waitKey(30) == ord('q'):
		break

#Release the video capture object
cap.release()
cv2.destroyAllWindows