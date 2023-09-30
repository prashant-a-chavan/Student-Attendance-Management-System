from tkinter import *
from tkinter import messagebox

class project:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1250x650')
        self.root.title('Student Page')

        self.bgImg = PhotoImage(file='photo3.png')
        self.d = Label(self.root,image=self.bgImg,bg='black')
        self.d.pack()

        self.bgColor = 'aliceblue'

        self.fm = Frame(self.root,width=350,height=260,bg=self.bgColor)
        self.fm.place(x=430,y=200)

        # self.LabelTop = Label(self.fm,text="Enter details...",font=("Times New Roman",12),bg=self.bgColor)
        # self.LabelTop.place(x=130,y=10)

        self.labelName = Label(self.fm,text="Name : ",font=("Times New Roman",10),bg=self.bgColor)
        self.labelName.place(x=52,y=105)

        self.EntryName = Entry(self.fm,width=30,bd=2)
        self.EntryName.place(x=120,y=105)

        self.labelSRN = Label(self.fm,text="SR No. : ",font=("Times New Roman",10),bg=self.bgColor)
        self.labelSRN.place(x=50,y=70)

        self.EntryId = Entry(self.fm,width=30,bd=2)
        self.EntryId.place(x=120,y=70)


        self.btn1 = Button(self.fm,text="Submit",padx=13,pady=3,command=self.con,bg='#152138',fg='white',bd=3,width=8,activebackground='white',activeforeground='black',font=("",10))
        self.btn1.place(x=135,y=190)

        
    # def fun(self):
    #     self.con()
        

    def con(self):
        import mysql.connector
        conn = mysql.connector.connect(host="localhost",user="root",password="reposeful",database="python")
        cur = conn.cursor()
        try:
            q = f"select s.usn , s.name , count(a.usn) from students s, attendence a where s.usn=a.usn and s.name = '{self.EntryName.get()}' and s.usn='{self.EntryId.get()}' group by(a.usn);"
            
            cur.execute(q)
            d = cur.fetchall();
            per = ((d[0][2]/40)*100)
            if(per > 85):
                messagebox.showinfo('Eligible',f'Attended classes : {d[0][2]}   and perc : {per}')
            else:
                messagebox.showerror('Not Eligible',f'Attended classes : {d[0][2]}   and perc : {per}')

        except:
            messagebox.showerror('Error','Invalid user')
root = Tk()
# EntryId = Entry(root).grid(row=2,column=2)
p = project(root)
root.mainloop()
