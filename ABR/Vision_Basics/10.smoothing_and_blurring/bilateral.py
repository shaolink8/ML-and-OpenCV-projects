# USAGE
# python bilateral.py big_boss.JPG

# import the necessary packages
import sys
import cv2

#get the image
#img = sys.argv[1]

# load the image, display it, and construct the list of bilateral
# filtering parameters that we are going to explore
image = cv2.imread(r'C:\Users\Shaolin Kataria\Documents\GitHub\ML-and-OpenCV-projects\ABR\Vision_Basics\10.smoothing_and_blurring\big_boss.jpg')
cv2.imshow("Original", image)
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

# loop over the diameter, sigma color, and sigma space
for (diameter, sigmaColor, sigmaSpace) in params:
	# apply bilateral filtering and display the image
	blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
	title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
	cv2.imshow(title, blurred)
	cv2.waitKey(0)