import cv2

img = cv2.imread("path/image_name.png")

cv2.imshow("outputé,img)")
cv.waitkey(0) #the time to desplaying an image / 0 for always; others for times(1ms)

################################################################
cap = cv2.VideoCapture("path/ved.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("vedio", img)
    if cv2.waitkey(1) & 0xFF == ord(q):
        break
#################################################################
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)


while True:
    success, img = cap.read()
    cv2.imshow("vedio", img)
    if cv2.waitkey(1) & 0xFF == ord(q):
        break





