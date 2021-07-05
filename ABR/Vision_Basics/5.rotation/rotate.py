# USAGE
# python rotate.py minion.jpg

# import the necessary packages
import imutils
import cv2
import sys
import numpy as np

# load the image and show it
image = cv2.imread(r'C:\Users\Shaolin Kataria\Documents\GitHub\ML-and-ABR\ABR\Vision_Basics\5.rotation\minion.jpg')
cv2.imshow("Original", image)


# A simple function to rotate images
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)

for i in range (0,360,20):
	print ("Rotated Angle", i)
	rotated = imutils.rotate(image, i)
	cv2.imshow("Rotated", rotated)
	cv2.waitKey(0)
