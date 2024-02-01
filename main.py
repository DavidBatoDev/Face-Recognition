import cv2
import pickle
import face_recognition
import cvzone
import os
import numpy as np

print('setting up')
cap = cv2.VideoCapture(0) # 0 for default  camera
cap.set(3, 640) # for width 
cap.set(4, 480) # for height 

img_background = cv2.imread('Resources/background.png') # read the image

# Importing the mode images from the folder to the list
folder_mode_path = 'Resources/Modes' # path to the folder
mode_path_list = os.listdir(folder_mode_path) # list of files in the folder
img_mode_list = [] # list of images


for path in mode_path_list:
    img = cv2.imread(f'{folder_mode_path}/{path}') # read the image
    img_mode_list.append(img) # append the image to the list

# load the encoding file
print('Loading Encoding File...')
file = open('EncodeFile.p', 'rb') # open the file in read binary mode
encode_list_known_with_ids = pickle.load(file)
file.close() 
encode_list_known, faces_ids = encode_list_known_with_ids
print(faces_ids)
print('Encoding File Loaded')

print('Starting Webcam...')
while True:
    success, img = cap.read() # read the image

    img_small = cv2.resize(img, (0, 0), None, 0.25, 0.25) # resize the image to 1/4th of its size
    img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB) # convert the image to RGB

    face_current_frame = face_recognition.face_locations(img_small) # find the face locations in the image
    encode_current_frame = face_recognition.face_encodings(img_small, face_current_frame) # find the encodings of the faces in the image

    img_background[162:162+480, 55:55+640] = img # replace the background with the image by slicing the image
    img_background[44:44+633, 808:808 + 414] = img_mode_list[0] # replace the background with another image by slicing the image

    for encode_face, face_location in zip(encode_current_frame, face_current_frame):
        matches = face_recognition.compare_faces(encode_list_known, encode_face)
        face_distance = face_recognition.face_distance(encode_list_known, encode_face) 

        matched_index = np.argmin(face_distance) # find the index of the minimum value in the list
        
        if matches[matched_index]:
            print('Match Found')
            y1, x2, y2, x1 = face_location # unpack the tuple
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4 # multiply by 4 to get the original size of the image because we resized it
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1 # create a bounding box
            img_background = cvzone.cornerRect(img_background, bbox, rt=0)


    cv2.imshow('Webcam', img) # show the image
    cv2.imshow('Background', img_background) # show the image
    cv2.waitKey(1) # wait for key press for 1 millisecond