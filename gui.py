from tkinter import *
from attendance import *
from Functions import *
import tkinter.messagebox
from PIL import ImageTk, Image


def clickCapture():
    ans = tkinter.messagebox.askyesno("Confirm", "Do you want to capture image?")
    if ans:
        name = enterName.get()
        captureImage(name)


def startProgram():
    tkinter.messagebox.showinfo("Info", "Please wait a while, Processing your Database Images...")
    start()


root = Tk()
root.title('Facial Recognition Attendance Program (Alpha-Version V1.0)')
root.minsize(910, 695)
root.maxsize(910, 695)
root.configure(background="#000000")

heading = Label(root, text="Welcome to Automated Attendance System", fg='#CDCDCD', bg="#80182A")
heading.configure(font=("Cambria", 35))
heading.pack(fill="x")

img = ImageTk.PhotoImage(Image.open('venv/lib/src_images/runtime_ninjas.png'))
labelImage = Label(root, image=img, borderwidth=0)
labelImage.pack(pady=20)

enterName = Entry(root, fg="#440D16", bg="#CDCDCD")
enterName.configure(font=15)
enterName.pack()

btn1 = Button(root, text="Add Image to Database", fg="#CDCDCD", bg="#80182A", width=25, height=2, command=clickCapture).pack(pady=(5, 20))
btn2 = Button(root, text="Open Attendance Sheet", fg="#CDCDCD", bg="#80182A", width=25, height=2, command=openExcel).pack(pady=(0, 20))
btn3 = Button(root, text="Start Program", fg="#CDCDCD", bg="#80182A", width=25, height=2, command=startProgram).pack(pady=(0, 20))
btn4 = Button(root, text="Read Me", fg="#CDCDCD", bg="#80182A", width=25, height=2).pack(pady=(0, 20))

root.mainloop()




