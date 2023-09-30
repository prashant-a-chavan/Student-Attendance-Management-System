import tkinter as tk
from tkinter import messagebox
import subprocess

from tkinter import messagebox
def open_attendance(uid,pas):

    import mysql.connector
    conn = mysql.connector.connect(host="localhost",user="root",password="reposeful",database="python")
    cur = conn.cursor()
    try:
        q = "select id from login"
        cur.execute(q)
        vals = cur.fetchall()
        userIds = []
        for i in vals:
            userIds+=i
        q = "select pas from login"
        cur.execute(q)
        vals = cur.fetchall()
        userPas = []
        for i in vals:
            userPas+=i
        for i in range(len(userIds)):
            if(uid==userIds[i]):
                if(pas==userPas[i] and userIds[i] == 'sjce'):
                    subprocess.call(['python', 'AdminPage.py'])
                    root.destroy()
                    break
                elif(pas==userPas[i] and userIds[i] == 'mca'):
                    subprocess.call(['python','studentLogin.py'])
                    root.destroy()
                    break
        # for i in range(0,len(records)):
        #     if(i%2==0):
        #         userIds[e] = records[i]
        #         e+=1
        #     else:
        #         userPas[o] = records[i]
        #         o+=1
        # print(userIds)
        # print(records)
        else:
            messagebox.showerror('Error','Invalid user')
    except:
        messagebox.showerror('Error','Invalid user')

    # if (uid == 'sjce' and pas == '1234'):
    #     subprocess.call(['python', 'AdminPage.py'])
    # elif (uid == 'mca' and pas == '1234'):
    #     subprocess.call(['python','studentLogin.py'])
    # else:
    #     messagebox.askretrycancel('Wrong','Invalid UserName or password')


root = tk.Tk()
root.geometry('1250x650')
root.title("JSS Science and Technology University")

bgImg = tk.PhotoImage(file='finalLogin.png')
d = tk.Label(root,image=bgImg,bg='black')
d.place(x=0,y=0)

# fm = tk.Frame(width=530,height=300,padx=50,pady=50)
# fm.place(x=420,y=250)
label1 = tk.Label(root,text="User Gateway",bg='white',width=15,font=("Rockwell",20))
label1.place(x=480,y=240)

labelId = tk.Label(root,text="Enter User ID ",bg='white',width=15,font=("Rockwell",10))
labelPas = tk.Label(root,text="Enter password ",bg='white',width=15,font=("Rockwell",10))

uid = tk.Entry(root,width=20,font=("Rockwell",10))
pas = tk.Entry(root,show='*',width=20,font=("Rockwell",10))

labelId.place(x=450,y=330)
uid.place(x=580,y=330)
labelPas.place(x=450,y=370)
pas.place(x=580,y=370)




button = tk.Button(root, text="Login", padx=10,bg='#152138',fg='white',bd=3,width=8,activebackground='white',activeforeground='black',font=("",10), command=lambda: open_attendance(uid.get(),pas.get()))
button.place(x=540,y=430)

root.mainloop()