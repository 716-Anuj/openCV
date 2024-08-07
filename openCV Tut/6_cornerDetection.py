import cv2 as cv
import numpy as np

img = cv.imread('Photos/chessboard.png')
img = cv.resize(img, (0, 0), fx = 0.75, fy = 0.75)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# corner detection
# Shi-Tomasi Corner Detector & Good Features to Track
corner = cv.goodFeaturesToTrack(gray, 100, 0.01, 10)
corner = np.int0(corner)

for c in corner:
    x, y = c.ravel()
    cv.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corner)):
    for j in range(i+1, len(corner)):
        corner1 = tuple(corner[i][0])
        corner2 = tuple(corner[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv.line(img, corner1, corner2, color, 1)

cv.imshow('frame', img)
cv.waitKey(0)
cv.destroyAllWindows()