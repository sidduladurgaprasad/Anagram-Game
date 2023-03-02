import random
from functools import partial
from tkinter import*
from tkinter import ttk,messagebox
from level3 import level3
from tkinter.font import BOLD, Font 
from PIL import Image,ImageTk


meddict = {
    "ladies"  : "ideals",
    "sister"  : "resist",
    "comics"  : "cosmic",
    "potion"  : "option",
    "shower"  : "whores",
    "tablet"  : "battle",
    "friend"  : "finder",
    "points"  : "piston",
    "caller"  : "recall",
    "dealer"  : "leader",
    "vowels"  : "wolves",
    
    "disease" : "seaside",
    "kitchen" :"thicken",
    "manures"  : "surname",
    "shotgun ":"gunshot",
    "restful" : "fluster",
    "decimal" : "claimed",  
    "earring" : "angrier",

    "reserved" :" reversed",
    "stealing" : "genitals",
    "drawback" :"backward",
    "thousand": "handsout",
    "teardrop":"predator",
    
}

class level2:
    def __init__(self,root):
        self.ans=StringVar() 
        self.root1=root
        self.score=0
        self.qn=1
        self.root1.geometry("1370x800+0+0")
        #Title
        self.root1.title("Game-level2")
        #Background
        img1=Image.open(r"D:\EDUCATION\PROJECTS\Game\Images\main.jpg")
        img1=img1.resize((1380,800),Image.ANTIALIAS)
        self.picimg1=ImageTk.PhotoImage(img1)  
        bg_img1=Label(self.root1,image=self.picimg1)
        bg_img1.place(x=0,y=60,width=1380,height=700)
        #level-1bar
        tlabel1=Label(self.root1,text="LEVEL-2",font=("times new roman",35,"bold"),bg="blue",fg="white")
        tlabel1.place(x=0,y=0,width=1380,height=60)
        #displayscore
        qlabel1=Label(self.root1,text="Score:"+str(self.score)+"/5",font=("times new roman",25,""),bg="yellow")
        qlabel1.place(x=870,y=135,width=200,height=40)
        #select question randomly from easydict
        a = random.choice(list(meddict))
        an=meddict[str(a)]
        #quesion
        qlabel1=Label(self.root1,text="Question : "+str(self.qn),font=("",20,""))
        qlabel1.place(x=400,y=250,width=200,height=50)
        question1=Label(self.root1,text=a,font=("",20,""))
        question1.place(x=620,y=250,width=200,height=50)
        #answer
        qlabel1=Label(self.root1,text="Answer : ",font=("",20,""))
        qlabel1.place(x=400,y=320,width=200,height=50)
        rnoip1=ttk.Entry(self.root1,textvariable=self.ans,width=25,font=("",20,""),foreground="brown",justify='center')
        rnoip1.place(x=620,y=320,width=200,height=50)
        #submit button
        action_with_arg = partial(self.check, a)
        b11=Button(self.root1,text="Submit",command=action_with_arg,cursor="hand2",font=("times new roman",25,"bold"),bg="green",fg="white")
        b11.place(x=400,y=400,width=420,height=50)
           
    def next(self):
        if self.score<6:
            self.qn = self.qn + 1
            #Background
            img1=Image.open(r"D:\EDUCATION\PROJECTS\Game\Images\main.jpg")
            img1=img1.resize((1380,800),Image.ANTIALIAS)
            self.picimg1=ImageTk.PhotoImage(img1)  
            bg_img1=Label(self.root1,image=self.picimg1)
            bg_img1.place(x=0,y=60,width=1380,height=700)
            #level-1bar
            tlabel1=Label(self.root1,text="LEVEL-2",font=("times new roman",35,"bold"),bg="blue",fg="white")
            tlabel1.place(x=0,y=0,width=1380,height=60)
            #displayscore
            qlabel1=Label(self.root1,text="Score:"+str(self.score)+"/5",font=("times new roman",25,""),bg="yellow")
            qlabel1.place(x=870,y=135,width=200,height=40)
            #select question randomly from easydict
            a = random.choice(list(meddict))
            an=meddict[str(a)]
            #quesion
            qlabel1=Label(self.root1,text="Question : "+str(self.qn),font=("",20,""))
            qlabel1.place(x=400,y=250,width=200,height=50)
            question1=Label(self.root1,text=a,font=("",20,""))
            question1.place(x=620,y=250,width=200,height=50)
            #answer
            qlabel1=Label(self.root1,text="Answer : ",font=("",20,""))
            qlabel1.place(x=400,y=320,width=200,height=50)
            self.ans.set("")
            rnoip1=ttk.Entry(self.root1,textvariable=self.ans,width=25,font=("",20,""),foreground="brown",justify='center')
            rnoip1.place(x=620,y=320,width=200,height=50)
            #submit button
            action_with_arg = partial(self.check, a)
            b11=Button(self.root1,text="Submit",command=action_with_arg,cursor="hand2",font=("times new roman",25,"bold"),bg="green",fg="white")
            b11.place(x=400,y=400,width=420,height=50)
        
        if self.score==5:
            #Welcome to level 2
            img=Image.open(r"D:\EDUCATION\PROJECTS\Game\Images\main.jpg")
            img=img.resize((1380,800),Image.ANTIALIAS)
            self.picimg=ImageTk.PhotoImage(img)  
            bg_img=Label(self.root1,image=self.picimg)
            bg_img.place(x=0,y=60,width=1380,height=700)
            qlabel=Label(self.root1,text="CONGRATULATIONS",font=("times new roman",30,"bold"),bg="orange")
            qlabel.place(x=450,y=200,width=500,height=70)
            qlabel=Label(self.root1,text="YOU HAVE SUCCESSFULLY COMPLETED LEVEL-2",font=("",25,""))
            qlabel.place(x=200,y=375,width=1000,height=70)
            b1=Button(self.root1,text="ENTER TO LEVEL-3...",command=self.level3,cursor="hand2",font=("times new roman",25,"bold"),bg="green",fg="white")
            b1.place(x=500,y=520,width=400,height=100)
            
        if self.qn==23 and self.score!=5:
            img=Image.open(r"D:\EDUCATION\PROJECTS\Game\Images\main.jpg")
            img=img.resize((1380,800),Image.ANTIALIAS)
            self.picimg=ImageTk.PhotoImage(img)  
            bg_img=Label(self.root1,image=self.picimg)
            bg_img.place(x=0,y=60,width=1380,height=700)
            qlabel=Label(self.root1,text="BETTER LUCK NEXT TIME....",font=("times new roman",30,"bold"),bg="orange")
            qlabel.place(x=450,y=200,width=500,height=70)
    def check(self,a):
        if self.ans.get()=="":
            messagebox.showerror("ERROR","Please enter your answer",parent=self.root1)
        else:
            self.a=a
            #next button
            nextpg = partial(self.next)
            b11=Button(self.root1,text="Next Question",command=nextpg,cursor="hand2",font=("times new roman",25,"bold"),bg="blue",fg="white")
            b11.place(x=400,y=470,width=420,height=50)
            if self.ans.get() == meddict[str(a)]:
                #Result
                qlabel=Label(self.root1,text="Correct",font=("times new roman",15,"bold"),bg="green",fg="white")
                qlabel.place(x=930,y=350,width=200,height=40)
                qlabel=Label(self.root1,text="Your Answer : "+self.ans.get())
                qlabel.place(x=930,y=250,width=200,height=40)
                qlabel=Label(self.root1,text="Correct Answer : "+meddict[str(a)])
                qlabel.place(x=930,y=300,width=200,height=40)
                
                self.score = self.score + 1
                qlabel=Label(self.root1,text="Score:"+str(self.score)+"/5",font=("times new roman",25,""),bg="yellow")
                qlabel.place(x=870,y=135,width=200,height=40)
                
            else:
                #Result
                qlabel=Label(self.root1,text="InCorrect",font=("times new roman",15,"bold"),bg="red",fg="white")
                qlabel.place(x=930,y=350,width=200,height=40)
                qlabel=Label(self.root1,text="Your Answer : "+self.ans.get())
                qlabel.place(x=930,y=250,width=200,height=40)
                qlabel=Label(self.root1,text="Correct Answer : "+meddict[str(a)])
                qlabel.place(x=930,y=300,width=200,height=40)
            meddict.pop(str(a))
    
    def level3(self):
        self.newpage=Toplevel(self.root1)
        self.app=level3(self.newpage)
    
if __name__=="__main__":
    root1=Tk()
    obj=level2(root1)
    root1.mainloop()
