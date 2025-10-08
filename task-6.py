import cv2 as cv
import numpy as np

image = cv.imread("gun.jpg")
if image is None:
    raise SystemExit("Image not found.")

h, w = image.shape[:2]
new_w, new_h = int(w * 0.5), int(h * 0.5)
resized = cv.resize(image, (new_w, new_h), interpolation=cv.INTER_AREA)

M = cv.getRotationMatrix2D((new_w // 2, new_h // 2), -45, 1.0)
cos, sin = np.abs(M[0, 0]), np.abs(M[0, 1])
nW = int((new_h * sin) + (new_w * cos))
nH = int((new_h * cos) + (new_w * sin))

M[0, 2] += (nW / 2) - (new_w / 2)
M[1, 2] += (nH / 2) - (new_h / 2)

rotated = cv.warpAffine(resized, M, (nW, nH))

cv.imshow("Original", image)
cv.imshow("Resized", resized)
cv.imshow("Rotated", rotated)

cv.waitKey(0)
cv.destroyAllWindows()
