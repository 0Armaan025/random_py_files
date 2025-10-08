import cv2 as cv
import sys

#ok, this was a mistake program, I didn't realize that the task #2 mentioned (from the computer!);


# print(cv.__version__)

# img = cv.imread(cv.samples.findFile("       "))

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("bhai aapka camera khul nhi rha somehow, chck kro!")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print('retrieve nhi ho rha frame, dekhiye kya problem hai, exiting...')
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
