class spo2:
    def __init__(self):
        self.spo2_readings=0
        self.hr_readings=0
        self.ser_code=""
    def get_spo2_readings(self):
        return self.spo2_readings
    def get_hr_readings(self):
        return self.hr_readings
    def get_ser_code(self):
        return self.ser_code
    def set_spo2_readings(self,l_spo2_readings):
        self.spo2_readings=l_spo2_readings
    def set_hr_readings(self,l_hr_readings):
        self.hr_readings=l_hr_readings
    def set_ser_code(self,l_ser_code):
        self.ser_code = l_ser_code