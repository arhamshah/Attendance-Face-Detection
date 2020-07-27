import cv2
import webbrowser


def openExcel():
    webbrowser.open("Attendance.csv")


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



