import cv2
import numpy as np

# for utilize ip cam, descoment this line and add a ip.
# cap = cv2.VideoCapture("rtsp://ipdacamera")
cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	
	if ret:
		cv2.imshow("frame", frame)
		key = cv2.waitKey(1)

	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()
