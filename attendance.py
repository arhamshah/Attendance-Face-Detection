import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

def start():
    path = 'database'
    imageList = []
    personName = []
    dataList = os.listdir(path)

    for data in dataList:
        curImage = cv2.imread(f'{path}/{data}')
        imageList.append(curImage)
        curName = os.path.splitext(data)[0]
        personName.append(curName)

    def findEncoding(imageList, nameList):
        encodeList = []
        for img, name in zip(imageList, nameList):
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)
            if len(encode) > 0:
                encodeList.append(encode[0])
            else:
                print(f"{name}'s image is not proper please recapture it")
        return encodeList

    print('Starting Encoding of Know Images in Database...')
    encodedKnown = findEncoding(imageList, personName)
    print('Encoding of Known Images Completed...')


    def markAttendance(name):
        with open('Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList =[]
            for dataLine in myDataList:
                entry = dataLine.split(',')
                nameList.append(entry[0])
            if name not in dataLine:
                now = datetime.now()
                dt_string = now.strftime("%H:%M:%S")
                f.writelines(f'\n{name},{dt_string}')


    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        frameS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        frameS = cv2.cvtColor(frameS, cv2.COLOR_BGR2RGB)

        cv2.putText(frame, "Press Esc to Exit", (15, 450), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 2)

        curFaceFrame = face_recognition.face_locations(frameS)
        curEncoding = face_recognition.face_encodings(frameS, curFaceFrame)

        for encoding, faceFrame in zip(curEncoding, curFaceFrame):
            result = face_recognition.compare_faces(encodedKnown, encoding)
            faceDist = face_recognition.face_distance(encodedKnown, encoding)
            Index = np.argmin(faceDist)

            y1, x2, y2, x1 = faceFrame
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            if faceDist[Index] < 0.55:
                name = personName[Index].upper()
                print(name)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{name}', (x1, y1-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255, 0))
                markAttendance(name)
            else:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, f'unknown', (x1, y1-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))

        cv2.imshow("Webcam", frame)
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyWindow("Webcam")
            break



