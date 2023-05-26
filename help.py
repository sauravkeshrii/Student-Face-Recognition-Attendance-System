from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("HELPDESK")
        
        title_lbl = Label(self.root, text="HELPDESK",font=("times new roman",35,"bold"),bg="white",fg="green" )
        title_lbl.place(x=0,y=0,width=1530,height=45) 
        
        
        img_top=Image.open(r"D:\Projects\IIITDM Student Management System\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top = img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        # Developer Info
        help_label = Label(f_lbl,text="Email: sauravkeshridata@gmail.com",font=("times new roman",20,"bold"), bg="white")
        help_label.place(x=500, y=210)
        
        
        
        
        
if __name__ == '__main__':
    root = Tk()
    obj = Help(root)
    root.mainloop()         