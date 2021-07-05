# USAGE
# python load_display_save.py big_boss.jpg

# import the necessary packages
import argparse
import cv2
import sys

# Get the image
#image = sys.argv[1]

# load the image and show some basic information on it
img = cv2.imread(r'C:\Users\Shaolin Kataria\Documents\GitHub\ML-and-OpenCV-projects\ABR\Vision_Basics\2.load_display_again\big_boss.jpg')

print("width:",img.shape[1])
print("height:",img.shape[0])
print("channels:",img.shape[2])

# show the image and wait for a keypress
cv2.imshow("Big_boss", img)
cv2.waitKey(0)

# save the image -- OpenCV handles converting filetypes
# automatically
cv2.imwrite("big_boss_2.jpg", img)
