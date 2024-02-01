import cv2
import os

cap = cv2.VideoCapture(0) # 0 for default  camera
cap.set(3, 640) # for width size
cap.set(4, 480) # for height size

imgBackground = cv2.imread('Resources/background.png') # read the image

# Importing the mode images from the folder to the list
folderModePath = 'Resources/Modes' # path to the folder
modePathList = os.listdir(folderModePath) # list of files in the folder
imgModeList = [] # list of images
print(modePathList)
for path in modePathList:
    img = cv2.imread(f'{folderModePath}/{path}') # read the image
    imgModeList.append(img) # append the image to the list


while True:
    success, img = cap.read() # read the image

    imgBackground[162:162+480, 55:55+640] = img # replace the background with the image by slicing the image
    imgBackground[44:44+633, 808:808 + 414] = imgModeList[0] # replace the background with another image by slicing the image

    cv2.imshow('Webcam', img) # show the image
    cv2.imshow('Background', imgBackground) # show the image
    cv2.waitKey(1) # wait for key press for 1 millisecond