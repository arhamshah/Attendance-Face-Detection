import cv2
import webbrowser
import face_recognition
import os
from datetime import datetime


def findEncoding(imageList, nameList):
    encodeList = []
    for img, name in zip(imageList, nameList):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        if len(encode) > 0:
            encodeList.append(encode[0])
        else:
            encode.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            encodeList.append(encode[0])
            print(f"{name}'s image is not proper please recapture it")
    return encodeList


def markAttendance(name, path):
    with open(f'{path}', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for dataLine in myDataList:
            entry = dataLine.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            f.writelines(f'\n{name},{dt_string}')


def openExcelWebcam():
    webbrowser.open("AttendanceWebcam.csv")


def openExcelImage():
    webbrowser.open("AttendanceImage.csv")


def openExcelVideo():
    webbrowser.open("AttendanceVideo.csv")


def openReadme():
    webbrowser.open(f'{os.path.dirname(__file__)}/README.md')


def captureImage(name):
    while True:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cv2.putText(frame, "Press SpaceBar to Capture", (15, 450), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('Webcam', frame)
        key = cv2.waitKey(1)
        if key == 32:
            cv2.imwrite(f'database/{name}.jpg', frame)
            cv2.destroyWindow('Webcam')
            break
