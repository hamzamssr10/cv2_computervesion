import cv2

img = cv2.imread("path/img.png")
print(img.shape) #shape of an image
imgResize = cv2.resize(img, (300,200)) #reshape an image
print(imgResize)
imgCropped = img[0:200, 200:500]





cv2.imshow("Cropped",imgCropped)
cv2.imshow("resizer",imgResize)
cv2.imshow("image",img)
cv2.waitKey(0)

