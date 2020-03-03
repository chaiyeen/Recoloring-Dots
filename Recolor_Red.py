"""
Recolor red circles into those of orange and purple
Download OpenCV library before running

Chaiyeen(Yun) Oh
"""
import cv2
import numpy as np

#Load image HERE
image = cv2.imread("S3_A0_MR.jpg", cv2.IMREAD_UNCHANGED)

#Detect red & create mask of the region
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
lower_red = np.array([0,120,50])
upper_red = np.array([95,255,255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([170,120,70])
upper_red = np.array([180,255,255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)
mask1 = mask1+mask2

# Segment out the red
# To prevent from mixing colors when two images are added together
mask2= cv2.bitwise_not(mask1)
cropped_red = cv2.bitwise_and(image,image,mask=mask2) #results of image with black circles : no red

#orange
orange = cv2.imread('ff9900.jpg', cv2.IMREAD_UNCHANGED)
orange = cv2.resize(orange, (800,600)) # to combine with other image & mask later
orange_circles = cv2.bitwise_and(orange,orange,mask=mask1)
orange = cv2.add(orange_circles, image) #combining orange circles and the image

#purple
purple = cv2.imread('5200A3.jpg', cv2.IMREAD_UNCHANGED)
purple = cv2.resize(purple, (800,600)) # to combine with other image & mask later
purple_circles = cv2.bitwise_and(purple,purple,mask=mask1)
purple = cv2.add(purple_circles, cropped_red) #combining purple circles and the image

#Display RESULT
cv2.imshow('Loaded Image', image) # original image
cv2.imshow('orange', orange)
cv2.imshow('purple', purple)
cv2.waitKey(0)

#Write names of the orange and purple images HERE
#cv2.imwrite("S3_A0_MR_orange.jpg",orange)
#cv2.imwrite("S3_A0_MR_purple.jpg",purple)

cv2.destroyAllWindows()