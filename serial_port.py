import threading
import serial
from serial import Serial
import sys
import time
import threading
class SerialPort():

    
    def __init__(self, L_Port_St, L_Baud_Ln):
        self.spo2 = []
        self.hr_readings = []
        self.Sensors = []
        print(self.Sensors)
        self.Buffer = []
        print(self.Sensors)
        try:
            self.SerialPort = serial.Serial(
            port= L_Port_St,
            baudrate=L_Baud_Ln,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout = 0,
            print(self.Sensors)
        try:
            self.SerialPort = serial.Serial(
            port= L_Port_St,
            baudrate=L_Baud_Ln,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout = 0
            
            )
            
        except:
            print("No Serial Port Available")
            sys.exit()
        #if SerialPort.isOpen:
           # print ("Port Opened Successfully")
            )
        def handle_data(self,L_DataList_Ls):
            L_DataList_Ls.append(2)
            threading.Thread(target = self.serial_read , args=(self.SerialPort,),).start()
           
        def serial_read(self,s):
            self._Continue = True
            while self._Continue:
                self.bytestoread = []
                self.nBytesToRead = 0
                time.sleep(0.07)
                self.nBytesToRead = s.in_waiting
                if self.nBytesToRead > 0:
                    self.Buffer = s.read(self.nBytesToRead)
                    if self.nBytesToRead >21:
                        #self.ValidateProtocol()
                        s.flushInput()

         def validateprotocol(self):
            if self.Buffer[0] == 2 and self.Buffer[len(self.Buffer)- 1] == 3:
                #print(self.Buffer)
                self.L_Index_I = 0
                self.L_Buffer_Ls = ""
                self.L_StrCounter = 0
                self.L_Object1 = 0
                self.L_Object2 = 0
                self.L_SensorAddress = 0
                self.L_SensorAddress = self.Buffer[1]
                self.L_spo2 = []
                self.L_hr_recordings = []



