<h1 align="center">
  <a href="#"><img src="https://i.ibb.co/kKhF4n5/runtime-ninjas.png" alt="Logo of Program" width="200"></a>
  <br>
    Attendance-Face-Detection
  <br>
</h1>

<h3 align="center">Automate your Attendance Using Facial Recognition</h3>
  
<p align="center">
  <img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="made with python">
  <img src="https://forthebadge.com/images/badges/built-with-love.svg" alt="built with love">
</p>


<p align="center">
  <a href="#introduction">Introduction</a> •
  <a href="#requirement">Requirements</a>  •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a>               •
  <a href="#how-it-works">How it Works</a> •
  <a href="#thanks">Thanks</a>
</p>

---

## Introduction
Detect & Recognize Faces from Live Feed, Static Image or Video. Attendace is marked & saved in Csv format. 
Graphical User Interface is designed & build using [Tkinter](https://docs.python.org/3/library/tkinter.html).
Built using [face recognition library](https://github.com/ageitgey/face_recognition) that is using state of art [dlib](https://github.com/davisking/dlib)'s facial recogniton having 99.38% accuracy.

![](https://i.ibb.co/XX4SwGt/gui-img-1.jpg) 



## Requirements

- Python 3.3+
- macOs or Linux or Windows
- Cmake 

## Installation

### Get it up & running

- Download our program from [here](https://github.com/arhamshah/Attendance-Face-Detection/archive/master.zip)
- Unzip the downloaded zip file
- Install all the dependencies from the requirement.txt

### Building the source code

#### 1. Clone the repository
```sh
git clone https://github.com/arhamshah/Attendance-Face-Detection.git
cd Attendance-Face-Detection
```
#### 2. Install Cmake 
- MacOs or Linux
```sh
brew install cmake
```
- Windows

Install Cmake & build or download a pre-configured  enviorment of windows-vm [here](http://ml.cdyne.com/Deep_Learning_Ubuntu_16.04_16-bit_2018_update.tar.gz)

#### 3. Download & Install all the Dependencies
```sh
pip install -r requirements.txt
``` 

## Usage
Checkout [Video Tutorial](https://www.youtube.com/watch?v=72gLLY4-HEg&feature=youtu.be)
### Adding Image to the database

- In order to add a person to the database, Enter name in the text box & choose "Add Image to Database" option.
- Capture user's image & it would be saved in ```database/```.

### Marking Attendance Using Webcam

- Choose "Start Program with Live Camera" option & Attendance would be updated in ```attendanceWebcam.py```.

### Marking Attendance by Importing Image

- Choose "Import Image/Video" option & select folder where image is present. Attendance would be updated in ```attendanceImage.py```.

### Marking Attendance by Importing Video

- Choose "Import Image/Video" option & select video. Attendance would be updated in ```attendanceVideo.py```.

### Accessing Attendance 

- Choose "Open Attendance Sheet" option & select mode by which attendance is marked (i.e. live video, image, video).


## How it Works
Checkout article by Adam Geitgey on [Face Rencogniton](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78)
- Face is detected by Hog algorithm
- Face detected is encoded by 128 measurements & saved for recognition
- When program is initiated User's face is similar detected & encoded by 128 measurements
- Later these encoded measurements are compared for recognizing face from Database
- If encodings are matched, Attendance is written in Csv File with Name & Time  

##Thanks
- Adam Geitgey for creating [face-recognition](https://github.com/ageitgey/face_recognition) library to provide an easy way of using of dlib's state of art recognition model.
- Davis King for creating [dlib](https://github.com/davisking/dlib), which provides facial features, face encoding models & face detection algorithms.
- Shoutout to developers & contributors of OpenCv, Pillow, Pip, Numpy, Scikit-Image, Tkinter, Scipy.
