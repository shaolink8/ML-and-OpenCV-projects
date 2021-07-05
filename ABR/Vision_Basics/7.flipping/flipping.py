# USAGE
# python flipping.py minions.jpg

# import the necessary packages

import cv2
import sys


#img = sys.argv[1]
# load the image and show it
image = cv2.imread(r'C:\Users\Shaolin Kataria\Documents\GitHub\ML-and-OpenCV-projects\ABR\Vision_Basics\7.flipping\minion.jpg')
cv2.imshow("Original", image)

# flip the image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# flip the image along both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)