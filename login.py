from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import ImageTk
import os
import time

mydb=mysql.connector.connect(host='localhost',user='root',password='1234',database="db1")
cur=mydb.cursor()
class Notepad:
    def __init__(self,Window):
        self.root=Window
        self.root.title("Notepad")
        self.root.geometry("1350x700")
        self.root.iconbitmap(r'notepad-icon\favicon.ico')

        #Variable Declaration------------------------------------------------------------
        Statusvar=StringVar()
        Statusvar.set("  .Ready")
        
        #File-functions--------------------------------------------------
        def NewFile():
            Statusvar.set("Creating New File")
            Statusbar.update()
            time.sleep(0.5)
            global file
            root.title("Untitled-Notepad")
            file=None
            TextArea.delete(1.0,END)
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def OpenFile():
            Statusvar.set("Opening File")
            Statusbar.update()
            time.sleep(0.5)
            global file
            file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Doccuments","*.txt")])
            if file == "":
                file=None
            else:
                root.title(os.path.basename(file)+"-Notepad")
                TextArea.delete(1.0,END)
                f=open(file,"r")
                TextArea.insert(1.0,f.read())
                f.close()
                
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def SaveFile():
            Statusvar.set("Creating New File")
            Statusbar.update()
            time.sleep(0.5)
            global file
            if file==None:
                file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Doccuments","*.txt")])

                if file=="":
                    file=None
                else:
                    #save as new file
                    f=open(file,"w")
                    f.write(TextArea.get(1.0,END))
                    f.close()
                    root.title(os.path.basename(file)+"-Notepad")
            else:
                #save the file
                f=open(file,"w")
                f.write(TextArea.get(1.0,END))
                f.close()
            
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def quitApp():
            root.destroy()
            print("Exit")
        
        #Edit-Function------------------------------------------------------
        def undo():
            TextArea.event_generate(("<<Undo>>"))
        def Cut():
            Statusvar.set("Cutting")
            Statusbar.update()
            time.sleep(0.5)
            TextArea.event_generate(("<<Cut>>"))
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def Copy():
            Statusvar.set("Copping")
            Statusbar.update()
            time.sleep(0.5)
            TextArea.event_generate(("<<Copy>>"))
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def Paste():
            Statusvar.set("Pasting")
            Statusbar.update()
            time.sleep(0.5)
            TextArea.event_generate(("<<Paste>>"))
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def delete():
            Statusvar.set("deleting")
            Statusbar.update()
            time.sleep(0.5)
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def Find():
            Statusvar.set("Finding")
            Statusbar.update()
            time.sleep(0.5)
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def FindNext():
            Statusvar.set("Find Next")
            Statusbar.update()
            time.sleep(0.5)
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def FindPrevious():
            Statusvar.set("Find Previous")
            Statusbar.update()
            time.sleep(0.5)
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def Replace():
            Statusvar.set("Replace")
            Statusbar.update()
            time.sleep(0.5)
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def goto():
            Statusvar.set("Goto")
            Statusbar.update()
            time.sleep(0.5)
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def selectAll():
            Statusvar.set("Select All")
            Statusbar.update()
            time.sleep(0.5)
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def Time():
            Statusvar.set("Timing")
            Statusbar.update()
            time.sleep(0.5)
            Statusvar.set("  Ready")
            Statusbar.update()
            
        #Formate-Function----------------------------------------------------------------------
        def WordWrap():
            Statusvar.set("WordWrap")
            Statusbar.update()
            time.sleep(0.5)
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def Font():
            Statusvar.set("Font")
            Statusbar.update()
            time.sleep(0.5)
            Statusvar.set("  Ready")
            Statusbar.update()
            
        
        #View-Function-----------------------------------------------------------------------------
        def Zoom():
            Statusvar.set("Zooming")
            Statusbar.update()
            time.sleep(0.5)
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def StatusBar():
            Statusvar.set("Status-Bar")
            Statusbar.update()
            time.sleep(0.5)
            Statusvar.set("  Ready")
            Statusbar.update()
            

        #Help-Function:--------------------------------------------------------------------
        def viewhelp():
            Statusvar.set("You clicked on help")
            Statusbar.update()
            time.sleep(0.5)
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def SendFeed():
            #-------------variables--------------------------------------------------------------------------
            var1=IntVar()
            var2=IntVar()
            svalue=StringVar()
            #------------------------------------------------------------------------------
            #---------------function--------------------------------------------------------
            def submit():
                if  var1.get()!=0:
                    if svalue.get() is not None:
                        if var2.get() is not None or var2.get()!=0:
                                messagebox.showinfo("Feedback","Sending Your Feedback..\n\nYour name is %s"%svalue.get()+"\nYour Age is %s"%str(var1.get())+"\nYour Phone no is %s"%str(var2.get()))
                else:
                    messagebox.showinfo("Error","Please fills the required information!!!!!!")
                
                    
            #------------------------------------------------------------------------------ 
            Statusvar.set("You Sending Feedback")
            Statusbar.update()
            time.sleep(0.5)
            top=Toplevel()
            top.title("Feedback")
            top.geometry("400x300")
            #---------------   form-Code   ---------------------------------------------
            lab=Label(top,text="Fill the feedback")
            lab.grid(row=0,column=0,padx=10,pady=10,ipadx=10,ipady=10,sticky="E")
            l1=Label(top,text="Enter your Name:")
            l2=Label(top,text="Enter your Age:")
            l3=Label(top,text="Enter your Phone no:")
            E1=Entry(top,textvariable=svalue,relief=SUNKEN)
            E2=Entry(top,textvariable=var1,relief=SUNKEN)
            E3=Entry(top,textvariable=var2,relief=SUNKEN)
            l1.grid(row=1,column=0,padx=10,pady=10,ipadx=5,ipady=5)
            l2.grid(row=2,column=0,padx=10,pady=10,ipadx=5,ipady=5)
            l3.grid(row=3,column=0,padx=10,pady=10,ipadx=5,ipady=5)
            E1.grid(row=1,column=1,padx=10,pady=10,ipadx=5,ipady=5)
            E2.grid(row=2,column=1,padx=10,pady=10,ipadx=5,ipady=5)
            E3.grid(row=3,column=1,padx=10,pady=10,ipadx=5,ipady=5)
            #---------------button---------------------------------------------------
            submit=Button(top,text="Submit",command=submit,relief=RAISED)
            submit.grid(row=5,column=1,padx=10,pady=10,ipadx=5,ipady=5)
            top.mainloop()
            #------------------------------------------------
            Statusvar.set("  Ready")
            Statusbar.update()
            
        def About():
            Statusvar.set("You Clicked on About")
            Statusbar.update()
            time.sleep(0.5)
            messagebox.showinfo("Notepad","This Notepad is created by Satish\nVersion- 1.0\nConnect")
            Statusvar.set("  Ready")
            Statusbar.update()
        
        #Add textArea---------------------------------
        TextArea=Text(self.root,font="lucida 13")
        file=None
        TextArea.pack(expand=True,fill=BOTH)

        #Menubar-File-------------------------------------
        Menubar=Menu(self.root)
        filemenu=Menu(Menubar,tearoff=0)
        filemenu.add_command(label="New",command=NewFile)
        filemenu.add_command(label="Open",command=OpenFile)
        filemenu.add_command(label="Save",command=SaveFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=quitApp)
        Menubar.add_cascade(label="File",menu=filemenu)

        #Edit------------------------------------------------------------
        Edit=Menu(Menubar,tearoff=0)
        Edit.add_command(label="Undo",command=undo)
        Edit.add_separator()
        Edit.add_command(label="Cut",command=Cut)
        Edit.add_command(label="Copy",command=Copy)
        Edit.add_command(label="Pest",command=Paste)
        Edit.add_command(label="Delete",command=delete)
        Edit.add_separator()
        Edit.add_command(label="Find",command=Find)
        Edit.add_command(label="Find Next",command=FindNext)
        Edit.add_command(label="Find Previous",command=FindPrevious)
        Edit.add_command(label="Replace",command=Replace)
        Edit.add_command(label="goto",command=goto)
        Edit.add_separator()
        Edit.add_command(label="Select all",command=selectAll)
        Edit.add_command(label="Time/Date",command=Time)
        Menubar.add_cascade(label="Edit",menu=Edit)

        #Formate-----------------------------------------------------------------
        FormateMenu=Menu(Menubar,tearoff=0)
        FormateMenu.add_command(label="Word Wrap",command=WordWrap)
        FormateMenu.add_command(label="Font..",command=Font)
        Menubar.add_cascade(label="Formate",menu=FormateMenu)

        #View---------------------------------------------------------------------------
        ViewMenu=Menu(Menubar,tearoff=0)
        ViewMenu.add_command(label="Zoom",command=Zoom)
        ViewMenu.add_command(label="Status Bar",command=StatusBar)
        Menubar.add_cascade(label="View",menu=ViewMenu)

        #help----------------------------------------------------------------------------
        HelpMenu=Menu(Menubar,tearoff=0)
        HelpMenu.add_command(label="Viewhelp",command=viewhelp)
        HelpMenu.add_command(label="Send Feedback",command=SendFeed)
        HelpMenu.add_command(label="About Notepad",command=About)
        Menubar.add_cascade(label="Help",menu=HelpMenu)
        root.config(menu=Menubar)

        #adding Vertical scrollbar---------------------------------------------
        Scroll=Scrollbar(TextArea)
        Scroll.pack(side=RIGHT,fill=Y)
        Scroll.config(command=TextArea.yview)
        TextArea.config(yscrollcommand=Scroll.set)

        #adding Horizontal scrollbar
        """Scrollx=Scrollbar(TextArea)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrollx.config(command=TextArea.xview)
        TextArea.config(xscrollcommand=Scrollx.set)"""
        
        #Status-Bar-------------------------------------------------------------------
        Statusbar=Label(self.root,textvariable=Statusvar,relief=SUNKEN,anchor="w")
        Statusbar.pack(side=BOTTOM,fill=X)
        self.root.mainloop()
        
class login_system:
    def __init__(self,master,cur,mydb):
        self.master=master
        self.master.title("Login-System")
        self.master.geometry("1350x700+0+0")
        self.cur=cur
        self.mydb=mydb
        self.username_=StringVar()
        self.pass_=StringVar()
        
        def topDestroy():
            top.destroy()
        
        def login():
            user_verify=self.username_.get()
            pass_verify=self.pass_.get()
            s="SELECT username,password from login where username=%s and password=%s";
            self.cur.execute(s,[(user_verify),(pass_verify)])
            result=self.cur.fetchall()
            if self.username_.get()=="" or self.pass_.get()=="" :
                messagebox.showerror("Error","All fields are required!")
            elif result:
                messagebox.showinfo("successful",f"welcome {self.username_.get()}")
                global root
                root=Tk()
                Notepad(root)
                masterDestroy()
            else:
                messagebox.showerror("Error","invalid username or password")
           
            

        def Register():
            user=self.username_.get()
            pass_=self.pass_.get()
            query="insert into login(username,password) values(%s,%s)"
            self.cur.execute(query,[(user),(pass_)])
            if self.username_.get()=="" or self.pass_.get()=="" :
                messagebox.showerror("Error","All fields are required!")
            if self.username_.get()!="" or self.pass_.get()!="" :
                messagebox.showinfo("successful",f"{self.username_.get()} registered") 
            self.mydb.commit()
            topDestroy()
                
        def RegisterWindow():
            global top
            top=Toplevel()
            top.title("Registration..")
            top.geometry("500x500+525+100")
            user=Label(top,text="Enter username *").grid(row=0,column=0,pady=10,padx=10)
            pass_=Label(top,text="Enter password *").grid(row=1,column=0)
            Entry1=Entry(top,textvariable=self.username_).grid(row=0,column=1)
            Entry2=Entry(top,textvariable=self.pass_).grid(row=1,column=1)
            btn=Button(top,text="Register",bg="red",fg="yellow",command=Register)
            btn.grid(row=2,columnspan=2,padx=10,pady=10)
            
        #images
        self.bg_icon=ImageTk.PhotoImage(file="images/bg.jpg")
        bg_lbl=Label(self.master,text="satish",image=self.bg_icon).pack()
        self.user_icon=PhotoImage(file="images/user.png")
        self.pass_icon=ImageTk.PhotoImage(file="images/pass.png")
        self.logo_icon=ImageTk.PhotoImage(file="images/user2.png")
        title=Label(self.master,text="Login-System",font=("times new roman",40,"bold"),bg='red',relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        
        
        #frame
        loginFrame=Frame(self.master,bg='white')
        loginFrame.place(x=525,y=80)
        logolbl=Label(loginFrame,image=self.logo_icon,bd=0,bg="red").grid(row=0,columnspan=2,padx=10,pady=10)
        userlbl=Label(loginFrame,text="Username",bg='white',image=self.user_icon,compound=LEFT,font=("times new roman",10,"bold")).grid(row=1,column=0,padx=10,pady=10)
        passlbl=Label(loginFrame,text="Password",bg='white',image=self.pass_icon,compound=LEFT,font=("times new roman",10,"bold")).grid(row=2,column=0,padx=10,pady=10)
        txtUser=Entry(loginFrame,bd=5,relief=GROOVE,textvariable=self.username_,font=("times new roman",10,"bold")).grid(row=1,column=1,padx=10,pady=10)     
        txtPass=Entry(loginFrame,bd=5,relief=GROOVE,textvariable=self.pass_,font=("times new roman",10,"bold")).grid(row=2,column=1,padx=10,pady=10)     
        btnLogin=Button(loginFrame,width=15,text="Login",font=("times new roman",10,"bold"),fg="red",bg="yellow",command=login).grid(row=3,columnspan=2,padx=10,pady=10)
        btnRegister=Button(loginFrame,width=15,text="Register",font=("times new roman",10,"bold"),fg="red",bg="yellow",command=RegisterWindow).grid(row=4,columnspan=2,padx=10,pady=10)

    def masterDestroy(self):
        self.master.destroy()   
      
master=Tk()
obj=login_system(master,cur,mydb)
master.mainloop()
