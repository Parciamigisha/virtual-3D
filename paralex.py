import cv2
import numpy as np
import matplotlib.pyplot as plt

class Game:
  def __init__(self):
    # CONSTANTS
    self.SCREEN_WIDTH = 20
    self.SCREEN_HEIGHT = 10
    self.SCREEN_PIXEL_WIDTH = 1920
    self.SCREEN_PIXEL_HEIGHT = 1080
    self.DIST_USER_TO_SCREEN = 25 # distance from the screen
    self.DIST_SCREEN_TO_TUNNEL = 50
    self.TUNNEL_WIDTH = 50
    self.TUNNEL_HEIGHT = 25

    # TUNNEL - four rectangles:
    #RECT0 = [[],[]]                       # [[top left ],[bottom right]]
    self.RECT0 = ((-25,-12.5,75),(25,12.5,75))   # [[x,y,z],[x,y,z]]
    self.RECT1 = ((-25,-12.5,125),(25,12.5,125))
    self.RECT2 = ((-25,-12.5,175),(25,12.5,175))
    self.RECT3 = ((-25,-12.5,225),(25,12.5,225))

    self.LINE0 = ((-25,-12.5,75),(-25,-12.5,225))
    self.LINE1 = ((25,12.5,75),(25,12.5,225))
    self.LINE2 = ((-25,12.5,75),(-25,12.5,225))
    self.LINE3 = ((25,-12.5,75),(25,-12.5,225))

    # the frame variable will hold our display pixels
    self.frame = np.zeros([self.SCREEN_PIXEL_HEIGHT,
                          self.SCREEN_PIXEL_WIDTH,
                          3])                         # three colors
  def threeD2twoD(s, xyz):
    """Maps a 3d point to 2d screen. Assumes user is at (0,0,0).
    EXAMPLE: (25,12.5,75) --> (row,col)
    """
    obj_x, obj_y, obj_z = xyz
    screen_z = s.DIST_USER_TO_SCREEN
    #  screen_x    obj_x
    #  -------- = ----------
    #  screen_z    obj_z

    screen_x = obj_x * screen_z / obj_z
    screen_x_px = (1920/20)* screen_x
    row = 1920/2 + screen_x_px

    #  screen_y    obj_y
    #  -------- = ----------
    #  screen_z    obj_z

    screen_y = obj_y * screen_z / obj_z
    screen_y_px = (1080/10)* screen_y
    col = 1080/2 + screen_y_px

    return (int(row),int(col))

  def draw_rectangle(self, rect_coords):
    """Convert rectcoords from 3d to 2d, then call opencv rectangle"""
    tl_row, tl_col = self.threeD2twoD(rect_coords[0])
    br = self.threeD2twoD(rect_coords[1])

    cv2.rectangle(self.frame,(tl_row,tl_col),     # top left
              br,                  # bottom right
              (0,0,255),           # color
              2)                   # line thickness

  #-----------------------------------------------
  # TODO 1
  # INSERT DRAWLINE METHOD BELOW

  # INSERT DRAWLINE METHOD ABOVE
  # END TODO 1
  #-----------------------------------------------


  def display_tunnel(self):
    """ Draw the four rectangles for tunnel """

    # first draw a circle in the center of the screen as a "vanishing point"
    cv2.circle(self.frame,
               (960,540),      # center point
               5,              # radius
               (255,255,255),  # color
               -1)             # line thickness, -1 for fill

    self.draw_rectangle(self.RECT0)
    self.draw_rectangle(self.RECT1)
    self.draw_rectangle(self.RECT2)
    self.draw_rectangle(self.RECT3)

    #-----------------------------------------------
    # TODO 2:
    # Call the draw_line method below for each of: LINE0, LINE1, LINE2, LINE3

    # Call the draw_line method above
    # END TODO 2
    #-----------------------------------------------



  def start_loop(self):
    """Runs a while loop """
    while True:
      # get face position


      # zero frame
      self.frame = np.zeros([self.SCREEN_PIXEL_HEIGHT,
                            self.SCREEN_PIXEL_WIDTH,
                            3])                         # three colors

      # draw tunnel from user's perspective
      self.display_tunnel()

      # temp code start-------------
      cv2_imshow(self.frame)
      break
      # temp code stop--------------

      #cv2.imshow(self.frame)
      #if cv2.waitKey(1) == ord('q'):
      #  break

    print('game over')


my_game = Game()
my_game.start_loop()
row, col = my_game.threeD2twoD((25,12.5,75))
print(row,col)