import cv2 as cv
import random

img = cv.imread('Photos/profilepic.jpg')

# Give numpy array
print(type(img))

# row, col and channel
print(img.shape)

# accessing pixel values
print(img[0][45:400]) # first row and pixel between 45 and 400

# changing pixel color
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# copying and pasting part of image
tag = img[500:700, 600:900]
img[100:300, 650:950] = tag
 


cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
