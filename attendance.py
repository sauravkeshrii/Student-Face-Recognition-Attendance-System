from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")
        
        #=======================variables======================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        
        # first img
        img1 =Image.open(r"D:\Projects\IIITDM Student Management System\college_images\smart-attendance.jpg")
        img1 = img1.resize((800,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
        #second img
        img2=Image.open(r"D:\Projects\IIITDM Student Management System\college_images\iStock.jpg")
        img2 = img2.resize((800,200),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
        
        #bg img
        img3=Image.open(r"D:\Projects\IIITDM Student Management System\college_images\bg2.jpg")
        img3 = img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)
        
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="blue" )
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1480,height=600)
        
        # left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))        
        Left_frame.place(x=10, y=10, width=760, height=580)
        
        
        img_left=Image.open(r"D:\Projects\IIITDM Student Management System\college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((750,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=750,height=130)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=140,width=735,height=350)
        
        # labels entry
        
        # attendanceID
        attendanceId_label = Label(left_inside_frame, text="StudentID",font=("times new roman",13,"bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        attendanceID_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"), bg="white")
        attendanceID_entry.grid(row=0,column=1, padx=10, pady=5, sticky=W)
        
        
        # Roll
        roll_label = Label(left_inside_frame, text="Roll",font=("times new roman",13,"bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=10, sticky=W)
        
        roll_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"), bg="white")
        roll_entry.grid(row=0,column=3, padx=10, sticky=W)
        
        # name
        name_label = Label(left_inside_frame, text="Name",font=("times new roman",13,"bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, sticky=W)
        
        name_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"), bg="white")
        name_entry.grid(row=1,column=1, padx=10, sticky=W)
        
        # department
        department_label = Label(left_inside_frame, text="Department",font=("times new roman",13,"bold"), bg="white")
        department_label.grid(row=1, column=2,pady=5, padx=10, sticky=W)
        
        department_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"), bg="white")
        department_entry.grid(row=1,column=3, pady=5,padx=10, sticky=W)
        
        # Time
        time_label = Label(left_inside_frame, text="Time",font=("times new roman",13,"bold"), bg="white")
        time_label.grid(row=2, column=0,pady=5, padx=10, sticky=W)
        
        time_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"), bg="white")
        time_entry.grid(row=2,column=1, pady=5,padx=10, sticky=W)
        
        # Date
        date_label = Label(left_inside_frame, text="Date",font=("times new roman",13,"bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, sticky=W)
        
        date_entry=Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"), bg="white")
        date_entry.grid(row=2,column=3, padx=10, sticky=W)
        
        # attendance
        attendance_label = Label(left_inside_frame, text="Attendance Status",font=("comicsansns 13 bold"), bg="white")
        attendance_label.grid(row=3, column=0)
        
        self.atten_status = ttk.Combobox(left_inside_frame, width=20, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ["Status","Present","Absent"]
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)
        
        
        # Buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=308, width=735, height=35)
        
        
        save_btn = Button(btn_frame, text="Import csv", command=self.import_Csv, width = 18, font=("times new roman",13,"bold"), bg="blue", fg="white" )
        save_btn.grid(row=0,column=0)
        
        
        update_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width = 17, font=("times new roman",13,"bold"), bg="blue", fg="white" )
        update_btn.grid(row=0,column=1)
        
        delete_btn = Button(btn_frame, text="Update", width = 17, font=("times new roman",13,"bold"), bg="blue", fg="white" )
        delete_btn.grid(row=0,column=2)
        
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width = 18, font=("times new roman",13,"bold"), bg="blue", fg="white" )
        reset_btn.grid(row=0,column=3)
        
        
        
        
        # Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Attendance Details",font=("times new roman",12,"bold"))        
        Right_frame.place(x=780, y=10, width=685, height=580)
        
        
        # Buttons frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=660, height=475)
        
        #==================================Scroll Bar Table=========================
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id","roll","name","department","time","date","attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id", text="Attendance ID" )
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        
        self.AttendanceReportTable.column("id", width=100 )
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        
        
        
        # ================================fetch data ==============================
        
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    # import csv    
    def import_Csv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File","*.csv"),("ALL File","*.*")), parent=self.root)
        with open(fln) as myfile:
          csvread = csv.reader(myfile, delimiter=",")
          for i in csvread:
            mydata.append(i)
          self.fetchData(mydata)
          
    # export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data exported", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir= os.getcwd(), title="Open Csv", filetypes=(("CSV file","*.csv"),("ALL File","*.*")), parent=self.root)
            with open(fln, mode='w', newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported", "Data Exported successfully at "+os.path.basename(fln)+"😊")        
        
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)
  
    def get_cursor(self):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item()
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
    def update_data(self): 
        pass 
              # ye banana baaki h
        
        
if __name__ == '__main__':
    root = Tk()
    obj = Attendance(root)
    root.mainloop() 
    