import cv2 as cv

image = cv.imread("gun.jpg")

if image is None:
    raise SystemExit("Bruh. The image wasn’t found. Check the file path.")

cv.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 2)  # green rectangle with thickness 2

cv.imshow("Rectangle on Image", image)

cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("image_with_rectangle.jpg", image)

print("✅ Rectangle drawn and image saved as 'image_with_rectangle.jpg'")
