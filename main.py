import cv2
import os

cap = cv2.VideoCapture(0) # 0 for default  camera
cap.set(3, 640) # for width size
cap.set(4, 480) # for height size

img_background = cv2.imread('Resources/background.png') # read the image

# Importing the mode images from the folder to the list
folder_mode_path = 'Resources/Modes' # path to the folder
mode_path_list = os.listdir(folder_mode_path) # list of files in the folder
img_mode_list = [] # list of images
print(mode_path_list)
for path in mode_path_list:
    img = cv2.imread(f'{folder_mode_path}/{path}') # read the image
    img_mode_list.append(img) # append the image to the list


while True:
    success, img = cap.read() # read the image

    img_background[162:162+480, 55:55+640] = img # replace the background with the image by slicing the image
    img_background[44:44+633, 808:808 + 414] = img_mode_list[0] # replace the background with another image by slicing the image

    cv2.imshow('Webcam', img) # show the image
    cv2.imshow('Background', img_background) # show the image
    cv2.waitKey(1) # wait for key press for 1 millisecond