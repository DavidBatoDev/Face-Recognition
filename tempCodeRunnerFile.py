while True:
    success, img = cap.read() # read the image

    imgBackground[162:162+480, 55:55+640] = img # replace the background with the image by slicing the image

    cv2.imshow('Webcam', img) # show the image
    cv2.imshow('Background', imgBackground) # show the image
    cv2.waitKey(1) # wait for key press for 1 millisecond