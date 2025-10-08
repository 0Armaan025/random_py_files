import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile('gun.jpg'))

if img is None:
    sys.exit("can't read")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("gun.jpg",img)
