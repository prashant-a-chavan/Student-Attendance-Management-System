from tkinter import *
from tkinter import messagebox

class attendence:
    def __init__(self, master=None):
        self.root = root
        self.master = master

        self.bgImg = PhotoImage(file='attendenceImage2.png')
        self.d = Label(self.root,image=self.bgImg,bg='black')
        self.d.pack()

        self.frame = Frame(self.root,width=500,height=300,bg='#352c45',border=5)
        self.frame.place(x=360,y=160)
        self.root.geometry('1250x650')
        self.root.title('Attendence')
        self.LabelTop = Label(self.frame,text="Attendence...",font=("Timew New Roman",13),width=35,bg='white')
        self.LabelTop.place(x=80,y=10)
        # self.labelGap = Label(self.frame).grid(row=1,column=0)
        self.labelSRN = Label(self.frame,text="USN No. : ",font=("Times New Roman",11),bg='white')
        self.labelSRN.place(x=60,y=100)
        self.EntryId = Entry(self.frame,bd=3,font=("Times New Roman",11),width=30)
        self.EntryId.place(x=150,y=100)

        self.help = Button(self.frame,text="get HELP",padx=6,pady=2,command=self.helpMessage,font=("Times New Roman",10),foreground='black',background='lightyellow',activebackground='black',activeforeground='white')
        self.help.place(x=380,y=100)
        
        # self.attSubmit = Button(self.attTop,text="Submit",command=self.att,padx=5,pady=2,bg='#152138',fg='white',bd=3,width=8,activebacground='white',activeforeground='black')

        self.btn1 = Button(self.frame,text="Submit",padx=6,pady=2,command=self.fun,font=("Times New Roman",11),bg='#152138',fg='white',bd=3,width=8,activebackground='white',activeforeground='black')
        self.btn1.place(x=190,y=170)



    def helpMessage(self):
        import mysql.connector
        conn = mysql.connector.connect(host="localhost",user="root",password="reposeful",database="python")
        cur = conn.cursor()
        presentList = []
        absentList = []
        try:
            q = f'select usn from students order by usn';
            cur.execute(q)
            count = cur.fetchall()
            # print(len(count))
            for i in range(1,len(count)+1):
                self.trash = messagebox.askyesnocancel('Answer attendence',f'USN : {i}  present ?')
                # print(self.trash)
                if(self.trash==TRUE):
                    presentList.append(i)
                    q = f"insert into attendence (USN) values('{i}')"
                    cur.execute(q)
                    conn.commit()
                elif(self.trash==FALSE):
                    absentList.append(i)
                else:
                    break
            messagebox.showinfo('Absents',f'{absentList}')
        except:
            messagebox.showerror('Error','Something went wrong...!')



    def fun(self):
        import mysql.connector
        conn = mysql.connector.connect(host="localhost",user="root",password="reposeful",database="python")
        cur = conn.cursor()
        try:
            data = self.EntryId.get()
            q = f"insert into attendence (USN) values('{data}')"
            cur.execute(q)
            conn.commit()
            # self.label1 = Label(self.root,text = f"{data} is present",foreground="green",pady=5,font=("Times New Roman",10)).grid(row=6,column=2)
            messagebox.showinfo('attendence',f'USN : {data} attendence submited')
        except:
            messagebox.showerror('Error','Something went wrong...!')



root = Tk()
p = attendence(root)
root.mainloop()