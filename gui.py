from cgitb import text
from msilib.schema import File
from os import popen
from subprocess import getoutput
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from typing_extensions import Self
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

#import numpy as np
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from cv2 import *
from PyQt5.QtCore import QRect, Qt

#from Convolution_network import *
#from Final import *

root = tk.Tk()
root.iconbitmap(r'E:\enw\Application\new_gui_assets\top_icon.ico')
root.title("BT detection")


canvas = tk.Canvas(root, width=600, height=550)
canvas.grid(columnspan=3, rowspan=3)
canvas.configure(background='white')

#Title Text
title_text = tk.Label(root, text="BRAIN TUMOR", font=("Leelawadee"),background='white')
title_text.place(x=240,y=10)

#Logo1

logo=Image.open('E:/enw/Application/new_gui_assets/logo.png')
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image = logo

canvas.create_image(550, 90, image=logo)

#Logo2

logo2=Image.open('E:/enw/Application/new_gui_assets/logo2.jpg')
logo2=ImageTk.PhotoImage(logo2)
logo_label=tk.Label(image=logo2)
logo_label.image = logo2
canvas.create_image(70, 95, image=logo2)

#Instructions
instrutions = tk.Label(root, text="Press RUN and Select an Image on your computer", font=("Leelawadee"),background='white')
instrutions.place(x=130,y=430)

#center canvas
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(column=1, rows=1)
canvas.place(x=0,y=150)
bg_img=Image.open('E:/enw/Application/new_gui_assets/gradient.png')
bg_img=ImageTk.PhotoImage(bg_img)
canvas.create_image(200,150,image=bg_img)

def open_file():
    run_text.set("LOADING...")   
    file=askopenfile(mode='rb',title="Choose an Image", filetypes=[("image file","*.jpg")]) 
    run_text.set("RUN")
    root_text = file.name
    img=Image.open(file)
    img=img.resize((200,200))
    img=ImageTk.PhotoImage(img)
    e1=tk.Label(root)
    e1.grid(row=1,column=1)
    e1.image=img
    e1['image']=img    
    if file:
        print("File sucessfully loaded.")
        return(root_text)

#CloseButton
close_text = tk.StringVar()
close_btn = tk.Button(root,textvariable=close_text,command=lambda:close_window(),font=("Leelawadee"),bg="#61e3bc",fg="white",height=2,width=12)
close_text.set("CLOSE")
close_btn.place(x=310,y=480)

#ButtonRun
run_text=tk.StringVar()
run_btn=tk.Button(root,textvariable=run_text,command=lambda:getOutput(),font=("Leelawadee"),bg="#20bebe",fg="white",height=2,width=12)
run_text.set("RUN")
run_btn.place(x=170,y=480)

#Close 
def close_window():
        exit()

#PopUp_Tumor
def tumor_pop():
        global t_pop
        t_pop = Toplevel(root)
        t_pop.wm_overrideredirect(True)
        t_pop.title('Tumor')
        t_pop.geometry('%dx%d+%d+%d' % (550, 300, 500, 200))
        t_pop.config(bg="white") 
        intro1=tk.Label(t_pop, text="Tumor Detected!", font=("Leelawadee",20),background='white')
        intro1.place(x=180,y=150)

        global tumor
        tumor=PhotoImage(file="E:/enw/Application/new_gui_assets/tumor.png")
        my_frame1 =Frame(t_pop, width=50,height=50,bg="white")
        my_frame1.pack(pady=10)

        t_pic = Label(my_frame1,image=tumor,borderwidth=0)
        t_pic.grid(row=0,column=0)

        my_frame2=Frame(t_pop, width=20, height=0,bg="white")
        my_frame2.pack(side='bottom')

        t_btn = Button(my_frame2, text="Go back to dashboard", command=lambda:t_pop.destroy(),font=("Leelawadee"),bg="#1e63cb",fg="white",height=2,width=20)
        t_btn.grid(row=3, column=0,pady=20)

#PopUp_nonTumor
def nontumor_pop():

        global nt_pop
        nt_pop = Toplevel(root)
        nt_pop.wm_overrideredirect(True)
        nt_pop.geometry('%dx%d+%d+%d' % (550, 300, 500, 200))
        nt_pop.config(bg="white") 
        intro1=tk.Label(nt_pop, text="No Tumor Detected", font=("Leelawadee",20),background='white')
        intro1.place(x=170,y=150)

        global non_tumor
        non_tumor=PhotoImage(file="E:/enw/Application/new_gui_assets/non_tumor.png")
        my_frame1 =Frame(nt_pop, width=50,height=50,bg="white")
        my_frame1.pack(pady=10)

        nt_pic = Label(my_frame1,image=non_tumor,borderwidth=0)
        nt_pic.grid(row=0,column=0)

        my_frame2=Frame(nt_pop, width=20, height=0,bg="white")
        my_frame2.pack(side='bottom')

        nt_btn = Button(my_frame2, text="Go back to dashboard", command=lambda:nt_pop.destroy(),font=("Leelawadee"),bg="#1e63cb",fg="white",height=2,width=20)
        nt_btn.grid(row=3, column=0,pady=20)

#Button1 and Button2
#tumor_text=tk.StringVar()
#tumor_btn=tk.Button(root,textvariable=tumor_text,command=lambda:tumor_pop(),font=("Leelawadee"),bg="#20bebe",fg="white",height=1,width=10)
#tumor_text.set("Tumor")
#tumor_btn.place(x=170,y=280)

#ntumor_text=tk.StringVar()
#ntumor_btn=tk.Button(root,textvariable=ntumor_text,command=lambda:nontumor_pop(),font=("Leelawadee"),bg="#20bebe",fg="white",height=1,width=10)
#ntumor_text.set("non Tumor")
#ntumor_btn.place(x=70,y=280)

#output
def getOutput():   
        txt=open_file()
        print(txt)
        main_output = brain_tumor(txt)
        #image_size = (1,64*64*3)
        #pixmap2 = cv2.imread(txt, cv2.IMREAD_GRAYSCALE)
        #pixmap2 = pixmap2 / 255
        #pixmap2 = cv2.resize(pixmap2, image_size, interpolation=cv2.INTER_CUBIC)
        #pixmap2 = np.reshape(pixmap2, (64,64,3))
        #main_output = brain_tumor(pixmap2)
        print(main_output)
        if main_output == 0:
                nontumor_pop()    
        else:
                tumor_pop()
    
        #self.label2.setText(str(main_output))
        #self.label1.setAlignment(Qt.AlignCenter)
        

root.resizable(False, False) 
root.mainloop()
