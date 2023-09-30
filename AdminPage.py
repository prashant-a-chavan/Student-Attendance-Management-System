import tkinter as tk
import subprocess

def open_Ins():
    subprocess.call(['python','Insert_Students.py'])

def open_Att():
    subprocess.call(['python','attendence.py'])

def open_Ret():
    subprocess.call(['python','retrieve.py'])

root = tk.Tk()
root.geometry('1250x650')
root.title("Welcome Admin")

bgImg = tk.PhotoImage(file='b.png')
d = tk.Label(root,image=bgImg,bg='black')
d.place(x=0,y=0)

fm = tk.Frame(width=200,height=230,padx=50,pady=50,highlightbackground='white')
fm.place(x=480,y=220)
p = tk.Label(fm,image=bgImg)


buttonIns = tk.Button(fm, text="Insert Students", padx=10,bg='#f9d1ff',fg='black',bd=3,width=10,activebackground='white',activeforeground='black',font=("",10), command=open_Ins)
buttonAtt = tk.Button(fm, text="Attendence", padx=10,bg='#f9d1ff',fg='black',bd=3,width=10,activebackground='white',activeforeground='black',font=("",10), command=open_Att)
buttonRet = tk.Button(fm, text="Retrieve", padx=10,bg='#f9d1ff',fg='black',bd=3,width=10,activebackground='white',activeforeground='black',font=("",10), command=open_Ret)
buttonIns.place(x=0,y=0)
buttonAtt.place(x=0,y=50)
buttonRet.place(x=0,y=100)


root.mainloop()