from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>', self.enter_func)
        
        main_frame = Frame(self.root, bd=4, bg="powder blue", width=610)
        main_frame.pack()
        
        
        
        img_chat = Image.open('D:\Projects\IIITDM Student Management System\chat.jpg')
        img_chat = img_chat.resize((200,70), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_chat)
        
        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730,compound=LEFT, image= self.photoimg, text='ASK ME', font=('arial',30,'bold'), fg='green', bg='white')
        Title_label.pack(side=TOP)
        
        #text Area with scrollbar
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20, bd=3, relief= RAISED, font=('arial',14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()
        
        # button & entry box
        
        btn_frame = Frame(self.root, bd=4, bg="white", width=730)
        btn_frame.pack()
        
        label = Label(btn_frame, text="Kindly Type Something!", font=('arial',13), fg='green', bg='white')
        label.grid(row=0, column=0, padx=5, sticky=W)
        
        self.entry = StringVar()
        self.entry1 = ttk.Entry(btn_frame,textvariable=self.entry, width=40,font=('arial',13,'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)
        
        self.send = Button(btn_frame, text="Send",command=self.send,font=('arial',13,'bold'), width=8, bg='green')
        self.send.grid(row=0, column=2, padx=5, sticky=W)
        
        self.clear = Button(btn_frame, text="Clear Data",command=self.clear,font=('arial',13,'bold'), width=8, bg='red', fg='white')
        self.clear.grid(row=1, column=0, padx=5, sticky=W)
        
        self.msg=''
        self.label_1 = Label(btn_frame, text=self.msg, font=('arial',13), fg='green', bg='white')
        self.label_1.grid(row=1, column=1, padx=5, sticky=W)
        
    #=============== Functions ========================    
    
    def enter_func(self, event):
        self.send.invoke()
        self.entry.set('')
        
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')
    
    def send(self):
        send = '\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END, '\n'+send)
        self.text.yview(END)
        
        if (self.entry.get()==''):
            self.msg = "Please enter something dude!"
            self.label_1.config(text=self.msg, fg='red')
            
        else:
            self.msg = ''
            self.label_1.config(text=self.msg, fg='red')
        
        if (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')
        
        elif(self.entry.get() =="hi"):
            self.text.insert(END, "\n\n"+"Bot: Hello")
        
        elif (self.entry.get()=="How are you?"):
            self.text.insert(END, "\n\n"+"Bot: fine and you")
        
        elif (self.entry.get()=="Fantastic"):
            self. text. insert (END, "In\n"+"Bot: Glad! You are loving it.")
            
        elif (self.entry. get () == "Who created you?"):
            self. text. insert (END, "In\n"+"Bot: Saurav Keshri")
            
        elif (self.entry. get () == "Who are you?"):
            self. text. insert (END, "\n\n"+"Bot: I am an A.I. bot. \n My name is Kriti.")
            
        elif (self.entry. get () == "Can you speak Maithili?"):
            self. text. insert (END, "\n\n"+"Bot: I'm still learning it.")
            
        elif (self.entry. get () == "What is machine learning?"):
            self. text. insert (END, "\n\n"+"Bot: Machine learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy.")

        elif (self.entry. get () == "How does face recognition work?"):
            self. text. insert (END, "\n\n"+"Bot: Facial recognition is a way of\nrecognizing a human face through technology. A facial recognition\nsystem uses biometrics to map facial features from a photograph\nor video. It compares the information\nwith a database of known faces to find\na match.")
        
        elif (self.entry. get () == "What is Python Programming?"):
            self. text. insert (END, "\n\n"+"Bot: Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming.")
            
        elif (self.entry. get () == "What is chatbot?"):
            self. text. insert (END, "\n\n"+"Bot: A chatbot or chatterbot is a software application used to conduct an online chat conversation via text or text-to-speech, in lieu of providing direct contact with a live human agent.")
        
        elif(self.entry.get()=="bye"):
            self.text.insert(END,"\n\n"+"Bot: Thank you for chatting with me.")
            
        elif(self.entry.get() =="Face Detection"):
            self.text.insert(END, "\n\n"+"Bot: The face detection is generally considered as finding the faces (location and size) in an image and probably extract them to be used by the face detection algorithm.")
        
        elif(self.entry.get()=="Face Recognition"):
            self.text.insert(END,"\n\n"+"Bot: The face recognition algorithm is used in finding features that are uniquely described in the image. The facial image is already extracted, cropped, resized, and usually converted in the grayscale.")
        
        elif(self.entry.get()=="Saurav Keshri"):
            self.text.insert(END,"\n\n"+"Bot: Saurav Keshri is the creator of my world.")
            
        elif(self.entry.get()=="Where are you?"):
            self.text.insert(END,"\n\n"+"Bot: Heaven! Well, Some may call it IIITDM Kurnool.")
            
        elif(self.entry.get()=="Director of IIITDM Kurnool"):
            self.text.insert(END,"\n\n"+"Bot: D V L N Somayajulu")
            
        elif(self.entry.get()=="Am i beautiful?"):
            self.text.insert(END,"\n\n"+"Bot: Ofcos! my baby girl.")
            
        else:
            self.text.insert(END,"\n\n"+"Bot: Sorry I didn't get it. I'm still in learning phase.")
          
if __name__=='__main__':
    root = Tk()
    obj= ChatBot(root)
    root.mainloop()
    
    

