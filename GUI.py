
import tkinter as tk
from tkinter import ttk,Canvas,Frame,BOTH
from tkinter.messagebox import showinfo
from tkinter import *
from matplotlib.figure import Figure
from spo2 import spo2
from db import db
from serial_port import SerialPort 
class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        mydb = db()
        #mydb.creat_table()
        current_data = spo2()
        current_data.set_ser_code("1206")
        current_data.set_spo2_readings(95)
        current_data.set_hr_readings(76)
        mydb.insert_data(current_data)
        result_data = mydb.read_data()
        #configure the root window
        #self.title('My Awesome App')
        current_port=SerialPort('com1',9600)
        self.root = Tk() 
        row_count=0
        self.e = Entry(self.root,width=20,fg="blue",font=('arial',16,'bold'))
        self.e.grid(row=row_count, column=0)
        self.e.insert(0,"spo2")
        self.e = Entry(self.root,width=20,fg="blue",font=('arial',16,'bold'))
        self.e.grid(row=row_count, column=1)
        self.e.insert(0,"hr_readings")
        row_count+=1
        for row in result_data :
            self.e = Entry(self.root,width=20,fg="blue",font=('arial',16,'bold'))
            self.e.grid(row=row_count, column=0)
            self.e.insert(0,row.get_spo2_readings())
            self.e = Entry(self.root,width=20,fg="blue",font=('arial',16,'bold'))
            self.e.grid(row=row_count, column=1)
            self.e.insert(0,row.get_hr_readings())
            self.but=Button(self.root,text="edit")
            self.but.grid(row=row_count, column=2)
            self.but["command"]=self.button_clicked
            row_count+=1

    def button_clicked(self):
        showinfo(title='information',message='button has been clicked')
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()


class Start_Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

class Start_Page1(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
