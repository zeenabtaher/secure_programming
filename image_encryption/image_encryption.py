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
        ##printing image details to make confirm opening
        print(file1) 
        file_name=file1.name
        print(file_name)
        
        ##Confirm the key entered by user before opening image
        key=entry1.get(1.0,END)
        print(file_name,key)
        
        ##Extract data from the image
        openFile=open(file_name,'rb')##rb method will read the data in byte format
        image=openFile.read()
        openFile.close()
        
        ##Converting image data to byte array
        image=bytearray(image)
        ##Enumerate method to define the key for each value of image variable
        for index, values in enumerate(image):
            ##zor operator to encryp and decrypt
            ##position of each value and then value itself
            image[index]=values^int(key) 
        fi1=open(file_name, 'wb') ##Wb method writing data
        fi1.write(image)
        fi1.close()
        
        
        

##Button to open file dialog box for submit key value
b1=Button(root,text="encrypt", command=encrypt_image)
b1.place(x=70, y=10)

entry1=Text(root,height=1,width=10)
entry1.place(x=50, y=50)

root.mainloop()



