from tkinter import *
from tkinter import messagebox
class project:
    
    def __init__(self,root):
        self.root = root
        self.root.geometry('1270x650')
        self.root.title('Attendence')


        self.bgImg = PhotoImage(file='photo2.png')
        self.d = Label(self.root,image=self.bgImg,bg='black')

        self.All  = Frame(self.d,width=440,height=220,bg='#e6fffb')
        self.All.place(x=370,y=190)
        # self.root.attributes('-alpha',0.5)
        self.d.pack()


        # self.cmb = Combobox(root,width=50,height=30)
        # self.cmb.grid(row=0,column=0)
        # self.cmb.set('Empty list')
        self.box = Listbox(self.All,width=60,height=10,font=("",10))
        self.box.insert(0,"SRNO                      Names                 Attended      (perc)")
        self.box.place(x=5,y=5)
        photo = PhotoImage(file='background copy.png')
        self.btn1 = Button(self.All,text="Student List",padx=6,pady=2,command=self.fun,bg='#152138',fg='white',bd=3,width=8,activebackground='white',activeforeground='black')
        self.btn1.place(x=30,y=185)
        # self.sname = Entry(self.root,bd='2')
        # self.sname.insert(-1,'enter usn number')

        # # To clear placeholder text of entry widget  
        # self.sname.bind('<FocusIn>',lambda args:self.sname.delete('0','end'))

        # self.sname.grid(row=0,column=2)
        self.btn2 = Button(self.All,text="Search",padx=6,pady=2,command=self.funTP,bg='#152138',fg='white',bd=3,width=8,activebackground='white',activeforeground='black')
        self.btn2.place(x=165,y=185)

        self.highest = Button(self.All,text='Attendence by %',padx=6,pady=2,command=self.attTp,bg='#152138',fg='white',bd=3,width=14,activebackground='white',activeforeground='black')
        self.highest.place(x=290,y=185)

    
        # self.highest = Button(self.All,text='Regular Student',padx=6,pady=2,command=self.regularStud)
        # self.highest.place(x=170,y=185)

    def attTp(self):
        self.attTop = Toplevel(self.root,bg='white')
        self.attTop.geometry('250x100')
        self.lb = Label(self.attTop,text="Enter % : ")
        self.lb.place(x=25,y=25)
        self.perc = Entry(self.attTop,border=2)
        # self.perc.insert(-1,'Enter %')
        self.perc.place(x=90,y=25)
        self.attSubmit = Button(self.attTop,text="Submit",command=self.att,padx=5,pady=2,bg='#152138',fg='white',bd=3,width=8,activebackground='white',activeforeground='black')
        self.attSubmit.place(x=75,y=60)
        # To clear placeholder text of entry widget  
        # self.perc.bind('<FocusIn>',lambda args:self.perc.delete('0','end'))

    def funTP(self):
        self.top = Toplevel(self.root)
        self.top.geometry('250x100')
        
        self.label1 = Label(self.top,text="Enter USN : ")
        self.sname = Entry(self.top,fg='#808080',bd=2)
        self.sname.insert(-1,'Enter USN number')
        self.topBtn = Button(self.top,text="Search",command=self.fun2,padx=5,pady=2,bd=3)
        self.label1.place(x=10,y=20)
        self.sname.place(x=80,y=20)
        self.topBtn.place(x=80,y=60)

        # To clear placeholder text of entry widget  
        self.sname.bind('<FocusIn>',lambda args:self.sname.delete('0','end'))
        self.top.mainloop()

    def att(self):
        import mysql.connector
        conn = mysql.connector.connect(host="localhost",user="root",password="reposeful",database="python")
        cur = conn.cursor()
        try:
            count=0
            s = []
            presentList = []
            absentList = []

            print(self.perc.get())
            
            q = f"select s.usn , s.name , count(a.usn) from students s, attendence a where s.usn=a.usn group by(a.usn) having (count(a.usn)/40)*100>{self.perc.get()};"
            cur.execute(q)
            l = cur.fetchall()
            self.box.delete(1,END)
            # for i in cur:
                # ins = i[0]
                # self.box.insert(1,ins)
                # s =s + i[0] + " "
                # s.append(i[0]) 
                # count+=1
            print(l)
            self.attTop.destroy()
            for student in l:
                # self.box.insert(END, f"{student[0]}     |     {student[1]}     |     {student[2]}")
                v = '{:30s} {:30s} {}           ({:.1f}%)'.format(student[0], student[1],student[2],(student[2]/40)*100)
                self.box.insert(END,v)

            # messagebox.showinfo("Aligible Students",f"USN : {s}")
               
        except:
            messagebox.showerror("Alert","Not accessible...")



    def regularStud(self):
        import mysql.connector
        conn = mysql.connector.connect(host="localhost",user="root",password="reposeful",database="python")
        cur = conn.cursor()
        try:
            q = "select usn from attendence group by(usn) order by(count(usn)) desc limit 1"
            cur.execute(q)
            for i in cur:
                self.regularMessage = messagebox.showinfo("Regular Student",f"USN : {i[0]}")
                
        except:
            Label(self.root,text="Unable to access the values",foreground="red").grid(row=3,column=2)

    def fun2(self):
        import mysql.connector
        conn = mysql.connector.connect(host="localhost",user="root",password="reposeful",database = "python")
        cur = conn.cursor()
        try:
            # q = "select * from students where NAME = %s"
            # data = self.sname.get()
            # cur.execute(q,(data,))
            # print(self.sname.get())
        #     self.top = Toplevel(self.root)
        #     self.sname = Entry(self.top)
        #     self.sname.insert(-1,'enter usn number')

        # # To clear placeholder text of entry widget  
        #     self.sname.bind('<FocusIn>',lambda args:self.sname.delete('0','end'))
        #     self.sname.grid(row=0,column=0)
        #     self.top.mainloop()
            
            data = self.sname.get()
            q = f"select s.name,count(a.usn) from students s, attendence a where s.usn = a.usn and s.usn='{data}' group by(a.usn)"
            cur.execute(q)
            l = cur.fetchall()
            ll = int((l[0][1]/40)*100)
            self.top.destroy()
            messagebox.showinfo('student info',f'Name : {l[0][0]} , Attendence : {ll}%')
        except:
            messagebox.showerror('error',f'USN {self.sname.get()} details does not exists...')
    
    def fun(self):
        import mysql.connector
        conn = mysql.connector.connect(host="localhost",user="root",password="reposeful",database="python")
        cur = conn.cursor()
        try:
            q = "select s.usn , s.name , count(a.usn) from students s, attendence a where s.usn=a.usn group by(a.usn)"
            l =[]
            cur.execute(q)
            yy = 20
            # for i in cur:
                # ins = i[0] + "                                   " + i[1]
                # self.box.insert(1,ins)
            self.box.delete(1,END)
            l = cur.fetchall()
            print(l)
            for student in l:
                # self.box.insert(END, f"{student[0]}     |     {student[1]}     |     {student[2]}")
                v = '{:30s} {:30s} {}           ({:.1f}%)'.format(student[0], student[1],student[2],(student[2]/40)*100)
                self.box.insert(END,v)

                # self.lab = Label(self.box,text=f'{i[0]}').place(x=5,y=yy,width='100')
                # self.lab = Label(self.box,text=f'{i[1]}').place(x=106,y=yy,width='100')
                # yy +=22
            # print(l)
            # self.cmb = Combobox(root,width=50)
            # self.cmb['values'] = 
            # pusn = l[0]
            # pname = l[1]
            # pcount = l[2]
            # al = f'{pusn[0]}' +  f'{pname[0]}' + f'{pcount[0]}'
            # self.cmb['values']= al
            # self.cmb.set('All students')
            
        except:
            messagebox.showerror('error','Something went wrong...!')
root = Tk()
# EntryId = Entry(root).grid(row=2,column=2)
p = project(root)
root.mainloop()
