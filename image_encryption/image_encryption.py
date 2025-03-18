# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 18:46:46 2025

@author: zeena


"""
##Importing tkinter for using UI
from tkinter import *
from tkinter import filedialog

##Building encryption UI
root=Tk()
root.geometry("200x160")

##Function to choose image file
def encrypt_image():
    file1=filedialog.askopenfile(mode='r', filetype=[('jpg file','*.jpg')]) ##TODO add png file
    if file1 is not None:
        print(file1)

##Button to open file dialog box for submit key value
b1=Button(root,text="encrypt", command=encrypt_image)
b1.place(x=70, y=10)

entry1=Text(root,height=1,width=10)
entry1.place(x=50, y=50)

root.mainloop()



