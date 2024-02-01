import cv2
import face_recognition
import pickle
import os

# importing faces images from the folder to the list
folder_path = 'Images' # path to the folder
faces_path_list = os.listdir(folder_path) # list of files in the folder, returns a list of strings
img_list = [] # list of images
faces_ids = [] # list of ids


for path in faces_path_list:
    img = cv2.imread(f'{folder_path}/{path}') # read the image
    img_list.append(img) # append the image to the list
    faces_ids.append(path.split('.')[0]) # append the id to the list


def findEncodings(images_list): # function to find the encodings of the images
    encodeList = []
    for image in images_list:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convert the image to RGB
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print('Encoding Started')
encode_list_known = findEncodings(img_list) # list of encodings of the images
encode_list_known_with_ids = [encode_list_known, faces_ids] # list of encodings and ids of the images
print('Encoding Complete')


file = open('EncodeFile.p', 'wb') # open the file in write binary mode
pickle.dump(encode_list_known_with_ids, file) # dump the data to the file
file.close() # close the file
print('File Saved')