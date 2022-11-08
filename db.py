import mysql.connector as conn
import numpy as np
from spo2 import spo2


class db:
    def __init__(self):
        self.mydb= conn.connect(host = 'localhost',user = 'root' ,passwd = "Swapnil@123",database="spo2" )
        self.cursor = self.mydb.cursor()
    def creat_table(self):
        self.cursor.execute('''CREATE TABLE patient (id int(10) AUTO_INCREMENT PRIMARY KEY, ser_code varchar(50),pulse_rate varchar(50),o2 varchar(50))''')
    def insert_data(self,spo2_data):
        cursor = self.mydb.cursor(prepared=True)
        try:
            ins_str="INSERT INTO patient(ser_code,pulse_rate,o2) VALUES (%s,%s,%s)"
            values=(spo2_data.get_ser_code(),spo2_data.get_hr_readings(),spo2_data.get_spo2_readings())
            self.cursor.execute(ins_str,values)
            self.mydb.commit()
        except:
            self.mydb.rollback()
            
    def read_data(self):
        read_str = "SELECT * FROM patient"
        self.cursor.execute(read_str)
        records = self.cursor.fetchall()
        current_records = []
        if len(records)>0:
            for row in records:
                current_data = spo2()
                current_data.set_ser_code(row[1])
                current_data.set_hr_readings(row[2])
                current_data.set_spo2_readings(row[3])
                current_records.append(current_data)
        return current_records       







        #result = self.cursor.execute("INSERT INTO patient(ser_code,pulse_rate,o2) VALUES (%s,%s,%s)", ('12','34','56'))#(spo2_data.get_ser_code(),spo2_data.get_hr_readings(),spo2_data.get_spo2_readings()))
        print("Data insert successfully")

        

