import hearty as hp
import matplotlib.pyplot as mlt
hrdata = hp.get_data('patient', column_name='hr')
timer_data = hp.get_data('patient',column_name='timer')
frame = hp.get_samlerate_mstimer (timer_data)
datetime_data = hr.get_data('patient',column_name='datetime')
get_samplerate_mstimer_datatime(datetime_data, column_name='datetime')
frame =hr.get_samplerate_datatime(datetime_data, timeformat='%y-%m-%d %H:%M:%S.%f', 24-hour)
print(frame)
working_data, measure = hp.process(hedata, hp.get_samplerate_)