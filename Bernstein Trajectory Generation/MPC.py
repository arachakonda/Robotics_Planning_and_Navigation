import cvxopt
import matplotlib.pyplot as plt
import cv2 
import numpy as np

def PlotMap(  centers , start, goal , radius ):

	canvas = 255 * np.ones((100, 100, 3), np.uint8)

	cv2.circle(canvas, (int(start[0]), int(start[1])), radius, (0, 0, 255), -1)
	cv2.circle(canvas, (int(goal[0]), int(goal[1])), radius, (0, 0, 255), -1)
	cv2.circle(canvas, (int(centers[0]), int(centers[1])), radius, (0, 0, 255), -1)

	canvas = cv2.flip(canvas, 0)
	cv2.namedWindow('MPC Path', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('MPC Path', 100, 100)
	cv2.imshow('MPC Path', canvas)
	cv2.waitKey()



centers = [50,50 ]
start = [ 10,10]
goal = [80,80 ]
radius = 3 


PlotMap( centers ,start , goal ,  radius)





 










