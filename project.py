# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import Message ,Text
from tkinter import *
import tkinter.messagebox
import PIL
from PIL import ImageTk
from PIL import Image

window = tk.Tk()
window.title("Facial Emotion Recognition Using AI Based Music Player")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
 
#window.geometry('1280x720')
#window.configure(background='#3b5999')

bg= ImageTk.PhotoImage(file="./bg.jpg")
#Create a canvas
canvas= Canvas(window,width= 400, height= 200)
canvas.pack(expand=True, fill= BOTH)
#Add the image in the canvas
canvas.create_image(0,0,image=bg, anchor="nw")

window.wm_attributes("-transparentcolor", 'grey')

window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


#message = tk.Label(window, text="Facial Emotion Recognition Using AI Based Music Player" ,bg="#3b5999"  ,fg="white"  ,width=58  ,height=3,font=('times', 30, 'italic bold underline')) 
#message.place(x=10, y=15)


def sd():
        #window.destroy()
        import os        
        os.system('python DetectEmotion.py')


def emt():
        #window.destroy()
        import os        
        os.system('python emt.py')
      

socialdistance = tk.Button(window, text="Emotion", command=emt  ,fg="white"  ,bg="#607D8B"  ,width=20  ,height=2, activebackground = "#21759b" ,font=('times', 15, ' bold '))
socialdistance.place(x=900, y=300)

socialdistance = tk.Button(window, text="Start Music AI", command=sd  ,fg="white"  ,bg="#607D8B"  ,width=20  ,height=2, activebackground = "#21759b" ,font=('times', 15, ' bold '))
socialdistance.place(x=900, y=400)

quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="white"  ,bg="#607D8B"  ,width=20  ,height=2, activebackground = "#21759b" ,font=('times', 15, ' bold '))
quitWindow.place(x=1050, y=640)

 
window.mainloop()
