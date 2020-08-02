import cv2
import numpy as np
import face_recognition
import os
from Functions import findEncoding, markAttendance


def startImage(directoryPath):
    path = 'database'
    imageList = []
    personName = []
    dataList = os.listdir(path)

    for data in dataList:
        curImage = cv2.imread(f'{path}/{data}')
        imageList.append(curImage)
        curName = os.path.splitext(data)[0]
        personName.append(curName)

    print('Starting Encoding of Know Images in Database...')
    encodedKnown = findEncoding(imageList, personName)
    print('Encoding of Known Images Completed...')


    imageCheckList = []
    dataCheckList = os.listdir(directoryPath)
    for data in dataCheckList:
        curImage = cv2.imread(f'{directoryPath}/{data}')
        imageCheckList.append(curImage)


    for image in imageCheckList:
        imageS = cv2.resize(image, (0, 0), None, 0.25, 0.25)
        imageS = cv2.cvtColor(imageS, cv2.COLOR_BGR2RGB)

        curFaceFrame = face_recognition.face_locations(imageS)
        curEncoding = face_recognition.face_encodings(imageS, curFaceFrame)

        for encoding, faceFrame in zip(curEncoding, curFaceFrame):
            result = face_recognition.compare_faces(encodedKnown, encoding)
            faceDist = face_recognition.face_distance(encodedKnown, encoding)
            Index = np.argmin(faceDist)

            y1, x2, y2, x1 = faceFrame
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            if faceDist[Index] < 0.55 and result:
                name = personName[Index].upper()
                print(name)
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
                cv2.putText(image, f'{name}', (x1, y1 - 6), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0), 5)
                markAttendance(name, "AttendanceImage.csv")
            else:
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 3)
                cv2.putText(image, f'Unknown', (x1, y1 - 6), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 5)

    #image = cv2.resize(image, (0,0), None, 0.25, 0.25)
    cv2.imshow("Picture", image)
    cv2.waitKey(0)