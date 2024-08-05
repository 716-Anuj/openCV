import cv2 as cv
import os

# read image
img = cv.imread('Photos/profilepic.jpg', 0)

# resize
# img = cv.resize(img, (400, 400))

# resizing using pixel
img = cv.resize(img, (0, 0), fx = 0.5, fy = 0.5)

# rotate
img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)

# -1, cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is default flag.
# 0, cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode 
# 1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

# visualize image
cv.imshow('cat', img)
cv.waitKey(0)
cv.destroyAllWindows()