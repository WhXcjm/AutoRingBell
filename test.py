import os 
import time 
import ntplib 
c = ntplib.NTPClient()
response = c.request('ntp.ntsc.ac.cn') 
ts = response.tx_time 
_date = time.strftime('%Y-%m-%d',time.localtime(ts)) 
_time = time.strftime('%X',time.localtime(ts))
print('date {} && time {}'.format(_date,_time))
os.system('date {} && time {}'.format(_date,_time))