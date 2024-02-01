import cv2

cap = cv2.VideoCapture(0) # 0 for default camera
cap.set(3, 1280) # for width
cap.set(4, 720) # for height

while True:
    success, img = cap.read() # read the image
    cv2.imshow('Face Recognition', img) # show the image
    cv2.waitKey() # wait for key press