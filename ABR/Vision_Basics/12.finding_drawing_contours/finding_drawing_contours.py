# USAGE
# python finding_drawing_contours.py images/basic_shapes.png

# import the necessary packages
import numpy as np
import sys
import cv2
import imutils

#img = sys.argv[1]

#print (img)

# load the image and convert it to grayscale
image = cv2.imread(r'C:\Users\Shaolin Kataria\Documents\GitHub\ML-and-OpenCV-projects\ABR\Vision_Basics\12.finding_drawing_contours\basic_shapes.png')
print (image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# show the original image
cv2.imshow("Original", image)

# find all contours in the image and draw ALL contours on the image
cnts = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
clone = image.copy()
ctr = np.array(cnts).reshape((-1,1,2)).astype(np.int32)
cv2.drawContours(clone, [ctr], -1, (0, 255, 0), 2)
print("Found {} contours".format(len(cnts)))

# show the output image
cv2.imshow("All Contours", clone)
cv2.waitKey(0)

# re-clone the image and close all open windows
clone = image.copy()
cv2.destroyAllWindows()

# loop over the contours individually and draw each of them
for (i, c) in enumerate(ctr):
	print("Drawing contour #{}".format(i + 1))
	cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
	cv2.imshow("Single Contour", clone)
	cv2.waitKey(0)

# re-clone the image and close all open windows
clone = image.copy()
cv2.destroyAllWindows()

# find contours in the image, but this time keep only the EXTERNAL
# contours in the image
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
ctr2 = np.array(cnts).reshape((-1,1,2)).astype(np.int32)
cv2.drawContours(clone, ctr2, -1, (0, 255, 0), 2)
print("Found {} EXTERNAL contours".format(len(cnts)))

# show the output image
cv2.imshow("All Contours", clone)
cv2.waitKey(0)

# re-clone the image and close all open windows
clone = image.copy()
cv2.destroyAllWindows()

# loop over the contours individually
for c in ctr:
	# construct a mask by drawing only the current contour
	mask = np.zeros(gray.shape, dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)

	# show the images
	cv2.imshow("Image", image)
	cv2.imshow("Mask", mask)
	cv2.imshow("Image + Mask", cv2.bitwise_and(image, image, mask=mask))
	cv2.waitKey(0)
