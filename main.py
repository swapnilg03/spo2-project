from db import db 
from spo2 import spo2


def startup ():
    mydb = db()
    #mydb.creat_table()
    current_data = spo2()
    current_data.set_ser_code("1206")
    current_data.set_spo2_readings(95)
    current_data.set_hr_readings(76)
    mydb.insert_data(current_data)
    result_data = mydb.read_data()
    print(result_data[0].get_ser_code())
    myspo2 = spo2()




if __name__ =="__main__":
    startup()



