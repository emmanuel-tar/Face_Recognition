# import packages

import cv2
import numpy as np
import sqlite3
import os, numpy, PIL
from PIL import Image

# To Detect the faces in the camera
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default (1).xml')
cam = cv2.VideoCapture(0)  # 0 is for web Camera


# Sqlite for the Db
def insertorupdate(Id, Name, age):
    conn = sqlite3.connect('sqlite.db')  # connect database
    cmd = "select * from  students where ID=" + str(Id)
    cursor = conn.execute(cmd)  # cursor for executing the sql command
    isRecordExist = 0  # assume there is no record in our table
    for row in cursor:
        isRecordExist = 1
    if (isRecordExist == 1):
        conn.execute("update students set Name=? where Id=?", (Name, Id,))
        conn.execute("update students set age=? where Id=?", (age, Id))
    # If the record doesn't exist, insert into the students db
    else:
        conn.execute("insert into students (Id,Name,Age) values(?,?,?)", (Id, Name, age))
    conn.commit()
    conn.close()


# insert user defined values into the tables

Id = input('Enter Student Id: ')
Name = input('Enter Student Name: ')
age = input('Enter Student Age: ')

insertorupdate(Id, Name, age)

# detect face in the web camera

sampleNum = 0
while (True):
    ret, img = cam.read()  # Open the Camera
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # Convert Image to BGRGRAY COLOR IMAGE
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)  # Scale Faces
    for (x, y, w, h) in faces:
        sampleNum = sampleNum + 1  # if face is detected increments
        cv2.imwrite('dataset/user.' + str(Id) + '.' + str(sampleNum) + '.jpg', gray[y:y + h,
                                                                               x:x + w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.waitKey(100)  # delay time for image preview
        cv2.imshow('Face', img)
        cv2.waitKey(1)
        if (sampleNum > 20):
            break
cv2.release()
cv2.destroyAllWindows()
