#Libraries
from tkinter import *
from tkinter import messagebox,colorchooser

#Application Setup
root = Tk()
root.geometry("520x300+380+140")
root.title("Interest Calculator")
root.resizable(False,False)
root.configure(bg="light grey")

#Functions
def color():
    cls = colorchooser.askcolor(title="Select Color to change")
    root.configure(bg=cls[1])
    Principal.config(bg=cls[1])
    Rate.config(bg=cls[1])
    Time.config(bg=cls[1])
    Interest.config(bg=cls[1])
    btn1.config(bg=cls[1])
    btn2.config(bg=cls[1])
    btn3.config(bg=cls[1])

def calculate():
    p = int(Pentry.get())
    r = int(Rentry.get())
    t = int(Tentry.get())
    if(p=="" and r=="" and t==""):
        messagebox.showwarning("Blank Input","Please fill input here!")
    else:
        amount = (p*r*t)/100
        Label(text=f"{amount}",font="Monospace 20 bold",
              bg="light grey",fg="dark blue").place(x=200,y=225)

#Application Creation
img1 = PhotoImage(file="E:\\pyImages\\interest logo.png")
root.iconphoto(False,img1)

Principal = Label(root,text="Principal: ",font=("Monospace",15,"bold"),bg="light grey")
Principal.place(x=50,y=20)
Rate = Label(root,text="Rate of interest: ",font=("Monospace",15,"bold"),bg="light grey")
Rate.place(x=50,y=90)
Time = Label(root,text="Time(Years): ",font=("Monospace",15,"bold"),bg="light grey")
Time.place(x=50,y=160)
Interest = Label(root,text="Interest: ",font="Monospace 15 bold",bg="light grey")
Interest.place(x=50,y=230)

Pvalue = StringVar()
Rvalue = StringVar()
Tvalue = StringVar()

Pentry = Entry(root,textvariable=Pvalue,bd=4,fg="indigo",bg="white",
            font=("Monospace",20,"bold"),width=8)
Pentry.place(x=220,y=20)
Rentry = Entry(root,textvariable=Rvalue,bd=4,fg="indigo",bg="white",
            font=("Monospace",20,"bold"),width=8)
Rentry.place(x=220,y=90)
Tentry = Entry(root,textvariable=Tvalue,bd=4,fg="indigo",bg="white",
            font=("Monospace",20,"bold"),width=8)
Tentry.place(x=220,y=160)

btn1 = Button(root,text="Calculate",font=("Monospace",15,"bold"),bd=4,bg="light grey",
       activebackground="light grey",command=lambda: calculate())
btn1.place(x=380,y=20)
btn2 = Button(root,text="Exit",width=8,font=("Monospace",15,"bold"),bd=4,bg="light grey",
       activebackground="light grey",command=lambda: root.destroy())
btn2.place(x=380,y=90)
btn3 = Button(root,text="Color",width=8,font=("Monospace",15,"bold"),bd=4,bg="light grey",
       activebackground="light grey",command=lambda: color())
btn3.place(x=380,y=160)
root.mainloop()
