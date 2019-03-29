import cv2

face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml')

image = cv2.imread("images/people.jpg")

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(image_gray, scaleFactor=1.04, minNeighbors=9)
faces_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale()
for (x,y,w,h) in faces:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

image_size = cv2.resize(image, (960, 540)) 

cv2.imshow('image',image_size,)
cv2.waitKey()