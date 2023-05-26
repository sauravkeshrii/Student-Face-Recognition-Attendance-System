from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")
        
        title_lbl = Label(self.root, text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="green" )
        title_lbl.place(x=0,y=0,width=1530,height=45) 
        
        
        img_top=Image.open(r"D:\Projects\IIITDM Student Management System\college_images\dev.jpg")
        img_top = img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        #frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)
        
        img_bottom=Image.open(r"D:\Projects\IIITDM Student Management System\college_images\saurav2.webp")
        img_bottom = img_bottom.resize((200,200),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(main_frame, image=self.photoimg_bottom)
        f_lbl.place(x=300,y=0,width=200,height=200)
        
        
        # Developer Info
        dev_label = Label(main_frame,text="Saurav - Keshri",font=("times new roman",20,"bold"), bg="white")
        dev_label.place(x=0, y=5)
        
        dev_label = Label(main_frame,text="\n Resources You need: \n 1. i3 Laptop\n 2. Hands to type \n 3. Free Time \n Ignorance & Patience",font=("times new roman",16,"bold"), bg="white")
        dev_label.place(x=0, y=35)
        
        img_2=Image.open(r"D:\Projects\IIITDM Student Management System\college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img_2 = img_2.resize((500,390),Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        f_lbl = Label(main_frame, image=self.photoimg_2)
        f_lbl.place(x=0,y=210,width=500,height=390)
        
        
if __name__ == '__main__':
    root = Tk()
    obj = Developer(root)
    root.mainloop() 
    