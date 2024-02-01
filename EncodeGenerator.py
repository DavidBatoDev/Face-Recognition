import cv2
import face_recognition
import pickle
import os

# importing faces images from the folder to the list
folder_path = 'images' # path to the folder
faces_path_list = os.listdir(folder_path) # list of files in the folder
img_list = [] # list of images
print(faces_path_list)
for path in faces_path_list:
    img = cv2.imread(f'{folder_path}/{path}') # read the image
    img_list.append(img) # append the image to the list
