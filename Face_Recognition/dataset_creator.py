#import packages

import cv2
import numpy as np
import sqlite3

#To Detect the faces in the camera
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default (1).xml')
cam=cv2.VideoCapture(0)  #0 is for web Camera


#Sqlite for the Db
def insertorupdate(Id,Name,age):
    conn = sqlite3.connect('database.db') #connect database
    cmd='select * from  students where ID=+str(Id)'
    cursor=conn.execute(cmd)  #cursor for executing the sql command
    isRecordExist=0    #assume there is no record in our table
    for row in cursor:
        isRecordExist=1
    if(isRecordExist == 1):
        conn.execute('update students set Name=? where Id=?',(Name,Id,))
        conn.execute('update student set age=? where Id=?',(age,Id))
#If the record doesn't exist, insert into the students db
    else:
        conn.execute('insert into student (Id,Name,Age) values(?,?,?)',(Id,Name,age))
    conn.commit()
    conn.close()
