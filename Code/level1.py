import random
from functools import partial
from re import L
from tkinter import*
from tkinter import ttk,messagebox
from tkinter.font import BOLD, Font
from level2 import level2
from PIL import Image,ImageTk

easydict = {
   "car"  : "arc",
    "arm"  : "ram",
    "dog"  : "god",
    "cat"  : "act",
    
    "mile" : "lime",
    "dear" : "read",
    "evil" : "live",
    "rear" : "rare",
    "spot" : "tops",
    "salt": "last",
    "shoe": "hose",
    "lamb" : "balm",
    "heir" : "hire",
    
    "flesh": "shelf",
    "feels": "flees",
    "layer" : "early",
    "kills" : "skill",
    "items" : "times",
    "lapse" : "leaps",
    "lured" : "ruled",
    "ought" :"tough",
    "saint" : "stain",
    "glare" :"large",
    "dairy" : "diary",
    "waist" : "waits",
    "peach": "cheap",
    "heart": "earth",
    "night" :"thing",
    "viral" :"rival",
}

class level1:
    def __init__(self,root):
        self.ans=StringVar() 
        self.root=root
        self.score=0
        self.qn=1
        self.root.geometry("1370x800+0+0")
        #Title
        self.root.title("Game")
        #Background
        img=Image.open(r"D:\EDUCATION\PROJECTS\Game\Images\main.jpg")
        img=img.resize((1380,800),Image.ANTIALIAS)
        self.picimg=ImageTk.PhotoImage(img)  
        bg_img=Label(self.root,image=self.picimg)
        bg_img.place(x=0,y=60,width=1380,height=700)
        #level-1bar
        tlabel=Label(text="LEVEL-1",font=("times new roman",35,"bold"),bg="blue",fg="white")
        tlabel.place(x=0,y=0,width=1380,height=60)
        #displayscore
        qlabel=Label(text="Score:"+str(self.score)+"/5",font=("times new roman",25,""),bg="yellow")
        qlabel.place(x=870,y=135,width=200,height=40)
        #select question randomly from easydict
        a = random.choice(list(easydict))
        an=easydict[str(a)]
        #quesion
        qlabel=Label(text="Question : "+str(self.qn),font=("",20,""))
        qlabel.place(x=400,y=250,width=200,height=50)
        question=Label(text=a,font=("",20,""))
        question.place(x=620,y=250,width=200,height=50)
        #answer
        qlabel=Label(text="Answer : ",font=("",20,""))
        qlabel.place(x=400,y=320,width=200,height=50)
        rnoip=ttk.Entry(textvariable=self.ans,width=25,font=("",20,""),foreground="brown",justify='center')
        rnoip.place(x=620,y=320,width=200,height=50)
        #submit button
        action_with_arg = partial(self.check, a)
        b1=Button(text="Submit",command=action_with_arg,cursor="hand2",font=("times new roman",25,"bold"),bg="green",fg="white")
        b1.place(x=400,y=400,width=420,height=50)
           
    def next(self):
        if self.score<6:
            self.qn = self.qn + 1
            img=Image.open(r"D:\EDUCATION\PROJECTS\Game\Images\main.jpg")
            img=img.resize((1380,800),Image.ANTIALIAS)
            self.picimg=ImageTk.PhotoImage(img)
            
            bg_img=Label(self.root,image=self.picimg)
            bg_img.place(x=0,y=60,width=1380,height=700)
            qlabel=Label(text="Score:"+str(self.score)+"/5",font=("times new roman",25,""),bg="yellow")
            qlabel.place(x=870,y=135,width=200,height=40)
            a = random.choice(list(easydict))
            an=easydict[str(a)]
            #quesion
            qlabel=Label(text="Question : "+str(self.qn),font=("",20,""))
            qlabel.place(x=400,y=250,width=200,height=50)
            question=Label(text=a,font=("",20,""))
            question.place(x=620,y=250,width=200,height=50)
            #answer
            qlabel=Label(text="Answer : ",font=("",20,""))
            qlabel.place(x=400,y=320,width=200,height=50)
            self.ans.set("")
            rnoip=ttk.Entry(textvariable=self.ans,width=25,font=("",20,""),foreground="brown",justify='center')
            rnoip.place(x=620,y=320,width=200,height=50)
            #submit button
            action_with_arg = partial(self.check, a)
            b1=Button(text="Submit",command=action_with_arg,cursor="hand2",font=("times new roman",25,"bold"),bg="green",fg="white")
            b1.place(x=400,y=400,width=420,height=50)
        
        if self.score==5:
            #Welcome to level 2
            img=Image.open(r"D:\EDUCATION\PROJECTS\Game\Images\main.jpg")
            img=img.resize((1380,800),Image.ANTIALIAS)
            self.picimg=ImageTk.PhotoImage(img)  
            bg_img=Label(self.root,image=self.picimg)
            bg_img.place(x=0,y=60,width=1380,height=700)
            qlabel=Label(text="CONGRATULATIONS",font=("times new roman",30,"bold"),bg="orange")
            qlabel.place(x=450,y=200,width=500,height=70)
            qlabel=Label(text="YOU HAVE SUCCESSFULLY COMPLETED LEVEL-1",font=("",25,""))
            qlabel.place(x=200,y=375,width=1000,height=70)
            b1=Button(text="ENTER TO LEVEL-2...",command=self.level2,cursor="hand2",font=("times new roman",25,"bold"),bg="green",fg="white")
            b1.place(x=500,y=520,width=400,height=100)
            
        if self.qn==29 and self.score!=5:
            img=Image.open(r"D:\EDUCATION\PROJECTS\Game\Images\main.jpg")
            img=img.resize((1380,800),Image.ANTIALIAS)
            self.picimg=ImageTk.PhotoImage(img)  
            bg_img=Label(self.root,image=self.picimg)
            bg_img.place(x=0,y=60,width=1380,height=700)
            qlabel=Label(text="BETTER LUCK NEXT TIME....",font=("times new roman",30,"bold"),bg="orange")
            qlabel.place(x=450,y=200,width=500,height=70)
    def check(self,a):
        if self.ans.get()=="":
            messagebox.showerror("ERROR","Please enter your answer",parent=self.root)
        else:
            self.a=a
            #next button
            nextpg = partial(self.next)
            b1=Button(text="Next Question",command=nextpg,cursor="hand2",font=("times new roman",25,"bold"),bg="blue",fg="white")
            b1.place(x=400,y=470,width=420,height=50)
            if self.ans.get() == easydict[str(a)]:
                #Result
                qlabel=Label(text="Correct",font=("times new roman",15,"bold"),bg="green",fg="white")
                qlabel.place(x=930,y=350,width=200,height=40)
                qlabel=Label(text="Your Answer : "+self.ans.get())
                qlabel.place(x=930,y=250,width=200,height=40)
                qlabel=Label(text="Correct Answer : "+easydict[str(a)])
                qlabel.place(x=930,y=300,width=200,height=40)
                
                self.score = self.score + 1
                qlabel=Label(text="Score:"+str(self.score)+"/5",font=("times new roman",25,""),bg="yellow")
                qlabel.place(x=870,y=135,width=200,height=40)
                
            else:
                #Result
                qlabel=Label(text="InCorrect",font=("times new roman",15,"bold"),bg="red",fg="white")
                qlabel.place(x=930,y=350,width=200,height=40)
                qlabel=Label(text="Your Answer : "+self.ans.get())
                qlabel.place(x=930,y=250,width=200,height=40)
                qlabel=Label(text="Correct Answer : "+easydict[str(a)])
                qlabel.place(x=930,y=300,width=200,height=40)
            easydict.pop(str(a))
        
    def level2(self):
        self.newpage=Toplevel(self.root)
        self.app=level2(self.newpage)
if __name__=="__main__":
    root=Tk()
    obj=level1(root)
    root.mainloop()
