import cv2 as cv
import numpy as np

image = cv.imread("gun.jpg")
if image is None:
    raise SystemExit("Image not found — fix the path, champ.")

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)  # convert so channels match

combined = np.hstack((image, gray_bgr))
cv.imshow("Real | Grayscale", combined)

cv.waitKey(0)
cv.destroyAllWindows()
