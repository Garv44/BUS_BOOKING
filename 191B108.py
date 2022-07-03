from tkinter import *
from PIL import Image, ImageTk
import sqlite3

t=Tk()
t.title("BUS BOOKING SYSTEM")
t.geometry("500x500")

conn=sqlite3.connect("BUS.db")
cur=conn.cursor()
cur.execute("CREATE TABLE if not exists DADD(id INTEGER,FullName TEXT, Contactno INTEGER, Address TEXT ,Operator TEXT,Bustype TEXT,drom TEXT,Tod TEXT,Dat DATE,Dep_Time TEXT,Arr_Time TEXT,Fare INTEGER,Seats INTEGER,PRIMARY KEY (id AUTOINCREMENT))")

conn.commit()
conn.close()

def Addbus():
    t.destroy()
    t1=Tk()
    t1.title("BUS BOOKING SYSTEM")
    t1.geometry("500x500")
    f2=Frame(bg="#000000")
    f2.place(x=0,y=0,width=500,height=800)
    l1=Label(f2,text="Add Bus ",font=('Times',25),fg='yellow',bg='black')
    l1.pack()
    img = Image.open("BUS.jpg")
    resized= img.resize((150,150))
    new=ImageTk.PhotoImage(resized)
    l2 = Label(f2,image=new)
    l2.pack()
    b=Label(f2,text="BUS OPERATOR DETAILS",font=('Times',12),fg='yellow',bg='black').place(x=150,y=215)
    l3=Label(f2,text="Full Name",fg='yellow',bg='black').place(x=120,y=250)
    e=Entry(f2,fg='yellow',bg='black')
    e.place(x=240,y=250)
    l4=Label(f2,text="Contact no",fg='yellow',bg='black').place(x=120,y=275)
    e1=Entry(f2,fg='yellow',bg='black')
    e1.place(x=240,y=275)
    l5=Label(f2,text="Address",fg='yellow',bg='black').place(x=120,y=300)
    e2=Entry(f2,fg='yellow',bg='black')
    e2.place(x=240,y=300)
    def adddetails():
        def asa():
            conn=sqlite3.connect("BUS.db")
            cur=conn.cursor()
            
            cur.execute("INSERT INTO DADD(FullName,Contactno,Address,Operator,Bustype,drom,Tod,Dat,dep_Time,Arr_Time,Fare,Seats) values(?,?,?,?,?,?,?,?,?,?,?,?)",(e.get(),e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get()))
            
            conn.commit()
            conn.close()

            e.delete(0,END)
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            e6.delete(0,END)
            e7.delete(0,END)
            e8.delete(0,END)
            e9.delete(0,END)
            e10.delete(0,END)
            e11.delete(0,END)


        t1.geometry("500x900")
        l6=Label(f2,text="Operator",fg='yellow',bg='black').place(x=120,y=375)
        e3=Entry(f2,fg='yellow',bg='black')
        e3.place(x=240,y=375)
        l7=Label(f2,text="Bus type",fg='yellow',bg='black').place(x=120,y=400)
        e4=Entry(f2,fg='yellow',bg='black')
        e4.place(x=240,y=400)
        l8=Label(f2,text="From",fg='yellow',bg='black').place(x=120,y=425)
        e5=Entry(f2,fg='yellow',bg='black')
        e5.place(x=240,y=425)
        l9=Label(f2,text="To",fg='yellow',bg='black').place(x=120,y=450)
        e6=Entry(f2,fg='yellow',bg='black')
        e6.place(x=240,y=450)
        l10=Label(f2,text="Date",fg='yellow',bg='black').place(x=120,y=475)
        e7=Entry(f2,fg='yellow',bg='black')
        e7.place(x=240,y=475)
        l11=Label(f2,text="Dep Time",fg='yellow',bg='black').place(x=120,y=500)
        e8=Entry(f2,fg='yellow',bg='black')
        e8.place(x=240,y=500)
        l12=Label(f2,text="Arr Time",fg='yellow',bg='black').place(x=120,y=525)
        e9=Entry(f2,fg='yellow',bg='black')
        e9.place(x=240,y=525)
        l13=Label(f2,text="Fare",fg='yellow',bg='black').place(x=120,y=550)
        e10=Entry(f2,fg='yellow',bg='black')
        e10.place(x=240,y=550)
        l14=Label(f2,text="Seats",fg='yellow',bg='black').place(x=120,y=575)
        e11=Entry(f2,fg='yellow',bg='black')
        e11.place(x=240,y=575)
        def save():
            t1.destroy()            
            t=Tk()
            t.title("BUS BOOKING SYSTEM")
            t.geometry("500x500")
            Main()
        
        b5=Button(f2,text="Save",font=('Times',11,"bold"),fg='yellow',bg='black',bd=2,command=save)
        b5.place(x=270,y=600)
        t1.mainloop()
        
                    

    b4=Button(f2,text="Add Details",font=('Times',11,"bold"),fg='yellow',bg='black',bd=2,command=adddetails)
    b4.place(x=200,y=330)
    t1.mainloop()
    
    
def Search():       
    t.destroy()
    t1=Tk()
    t1.title("BUS BOOKING SYSTEM")
    t1.geometry("500x500")
    f2=Frame(bg="#000000")
    f2.place(x=0,y=0,width=500,height=800)
    l1=Label(f2,text="Search Bus ",font=('Times',25),fg='yellow',bg='black')
    l1.pack()
    img = Image.open("B2.jpg")
    resized= img.resize((150,150))
    new=ImageTk.PhotoImage(resized)
    l2 = Label(f2,image=new)
    l2.pack()
    
    b=Label(f2,text="SEARCH BUS ",font=('Times',12),fg='yellow',bg='black').place(x=200,y=205)

    bus_type_selection = StringVar()
    bus_type_selection.set("Bus Type")
    l4=Label(t1,text="Bus Type: ",fg='yellow',bg='black').place(x=70,y=230)
    bustype = ['AC','Non-AC','AC Sleeper','Non-Sleeper AC','All Types']
    OptionMenu(t1,bus_type_selection,*bustype).place(x=180,y=230)


    l1=Label(t1,text="From: ",fg='yellow',bg='black').place(x=70,y=270)
    frm = Entry(t1,fg='yellow',bg='black')
    frm.place(x=180,y=270)


    l2=Label(t1,text="To: ",fg='yellow',bg='black').place(x=70,y=300)
    destination=""
    destination= Entry(t1,fg='yellow',bg='black')
    destination.place(x=180,y=300)


    l3=Label(t1,text="Date(yyyy-mm-dd): ",fg='yellow',bg='black').place(x=70,y=330)
    date=""
    date = Entry(t1,fg='yellow',bg='black')
    date.place(x=180,y=330)
    
      
    def sech():
            t1.destroy()
            t=Tk()
            t.title("BUS BOOKING SYSTEM")
            t.geometry("500x500")
            Main()
        
    b5=Button(t1,text="Search",font=('Times',11,"bold"),fg='yellow',bg='black',bd=2,command=sech)
    b5.place(x=270,y=400)
    t1.mainloop()


def Main():
    f1=Frame(bg="#000000")
    f1.place(x=0,y=0,width=500,height=800)
    l1=Label(f1,text=" YELLOW BUS ",font=('Times',30),fg='yellow',bg='black')
    l1.pack()
    img = Image.open("B1.jpg")
    resized= img.resize((250, 250), Image.ANTIALIAS)
    new=ImageTk.PhotoImage(resized)
    l2 = Label(f1,image=new)
    l2.pack()
    btn1=Button(f1,text="Add Bus",font=('Times',15),fg='yellow',bg='black',bd=2,command=Addbus).place(x=20,y=400)
    btn2=Button(f1,text="Search Bus",font=('Times',15),fg='yellow',bg='black',bd=2,command=Search).place(x=380,y=400)
    
    t.mainloop()

Main()

t.mainloop()    


front = Tk()
front.geometry("950x350")
front.title("Bus Booking Service")
front.configure(bg="black")
Label(front,text="Project Title : Bus Booking System",font="bold 30",bg="black",fg="red").grid(row=0,column=0)
Label(front,text="",bg="black").grid(row=1,column=0)
Label(front,text="Developed as part of the course Advanced Programming Lab-1 & DBMS",font="bold 15",bg="black",fg="yellow").grid(row=2,column=0)
Label(front,text="",bg="black").grid(row=3,column=0)
Label(front,text="  Developed by: Garv Chaplot, 191B108, 7014966793, 191b108@juetguna.in",font="bold 20",bg="black",fg="yellow").grid(row=4,column=0)
Label(front,text="",bg="black").grid(row=5,column=0)
Label(front,text="***********************************************************************",font="bold 20",bg="black",fg="yellow").grid(row=6,column=0)
Label(front,text="",bg="black").grid(row=7,column=0)
Label(front,text="Project Supervisors: Dr Mahesh Kumar & Nilesh Patel",font="bold 20",bg="black",fg="yellow").grid(row=8,column=0)
Label(front,text="",bg="black").grid(row=9,column=0)

Label(front,text="Make mouse movement over this screen to close",font="bold 15",bg="black",fg="#FF0000").grid(row=10,column=0)


def close(e):
    front.destroy()
    
front.bind('<Motion>',close)

front.mainloop()