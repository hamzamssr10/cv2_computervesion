import cv2
import numpy as np


img = cv2.imread("peth/img.png")
kernel = np.ones((5,5), np.uint8)



imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("image",imgGray)
cv2.waitkey(0)



imgBlur = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("image",imgBlur)
cv2.waitkey(0)



imgCanny = cv2.Canny(img,100,100)
cv2.imshow(imagCanny)
cv2.waitkey(0)

imgDalation = cv2.dilate(imgCanny, kernel, iterations = 1)
cv2.imshow(imgDalation)
cv2.waitkey(0)

imgEroded = cv2.erode(imgDalation, kernel, iterations = 1)
cv2.imshow(imgDalation)
cv2.waitkey(0)


