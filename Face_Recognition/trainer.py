import os                   #read and write file
import cv2                  #Open Camera
import numpy as np          #Array
from PIL import Image       #Image file read and write

recognizer=cv2.face.LBPHFaceRecognizer_create()         #it recognise the face in camera
path="dataset"


def get_image_with_id(path):
    images_paths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    ids=[]
    for single_image_path in images_paths:
        faceImg=Image.open(single_image_path).convert('L')       #image converted into gray
        faceNp=np.array(faceImg,np.uint8)
        id=int(os.path.split(single_image_path)[-1].split(".")[1])
        print(id)
        faces.append(faceNp)
        ids.append(id)
        cv2.imshow('Training',faceNp)
        cv2.waitKey(10)
    return np.array(ids),faces
ids,faces=get_image_with_id(path)
recognizer.train(faces,id)
recognizer.save('recognizer/trainingdata.yml')
cv2.destroyAllWindows()



