import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Drawing a line
    img = cv.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv.line(img, (0, height), (width, 0), (0, 255, 0), 10)

    # rectangle
    img = cv.rectangle(img, (100, 100), (200, 200), (128, 128, 0), 10)

    # circle
    img = cv.circle(img, (width//2, height//2), (30), (255, 128, 255), 10)

    # text
    font = cv.FONT_HERSHEY_SIMPLEX
    img = cv.putText(img, 'Anuj Pradhan', (10, height-100), font, 2, (0, 0, 0), cv.LINE_AA, 5, cv.LINE_AA)

    cv.imshow('frame', img)

    if cv.waitKey(1) == ord('q'):
        break

cap.release
cv.destroyAllWindows