import pygame.mixer as mixer
import sys, time
argv = sys.argv
argc = len(argv)
print(argv)
def Play(s,wait=1):
	mixer.music.load("{}".format(s))
	mixer.music.play()
	if(wait):
		while(mixer.music.get_busy()):
			time.sleep(0.05)
if(argc==2):
	print("Solo Mode")
	mixer.pre_init(devicename="VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)")
	mixer.init()
	Play(argv[1])
	exit(0)
import ntplib, csv, re, os

# mixer.init()
# is_capture = 0  # zero to request playback devices, non-zero to request recording devices
# names = sdl2.get_audio_device_names()
# print("\n".join(names))

# "VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)"
lastUpdateofTime = -24
timeTable = []
logFile = 0
Delay0 = 0.05
Nxti=-1
Delay = Delay0

def log(s):
	global logFile
	if (logFile==0):
		logFile = open("schedule.log", 'a+')
	print(s,end='')
	logFile.write(str(s))
	logFile.flush()
	
def initTable():
	with open("schedule.csv") as f:
		tt = csv.reader(f)
		for i in tt:
			timeTable.append([list(map(int, i[1].split(':'))), i[0]])
	timeTable.sort()
	log(str(timeTable)+'\n')
	
def updateTime():
	try:
		c = ntplib.NTPClient()
		response = c.request('ntp.aliyun.com')
		ts = response.tx_time
		_date = time.strftime('%Y-%m-%d', time.localtime(ts))
		_time = time.strftime('%X', time.localtime(ts))
		os.system('date {} && time {}'.format(_date, _time))
		log('Updated time: date {} && time {}\n'.format(_date, _time))
		return True
	except KeyError:
		KeyboardInterrupt()
	except Exception as e:
		log('Failed to updated time:\n')
		log(e)
		return False
	
def getTime(n=2):
	global lastUpdateofTime
	lt=time.localtime()
	if (time.localtime().tm_hour - lastUpdateofTime != 0 and [lt.tm_hour, lt.tm_min]!=timeTable[Nxti][0]):
		updateTime()
		lt=time.localtime()
		lastUpdateofTime = lt.tm_hour
	if(n==2):
		return [lt.tm_hour, lt.tm_min]

def ramainTime(a,b):
	return (b[0]-a[0])*60+b[1]-a[1]

def updateDelay():
	global Delay
	tmp=Delay
	nowt=getTime()
	i=0
	while(i<len(timeTable)):
		if(ramainTime(nowt,timeTable[i][0])<0):
			i+=1
		else:
			break
	i%=len(timeTable)
	dt=ramainTime(nowt,timeTable[i][0])
	if(dt<0):
		Delay=3600
	else:
		global Nxti
		Nxti=i
		if(dt<=2):
			Delay=Delay0
		else:
			Delay=(dt-1)*60/2
	if(Delay!=tmp):
		log("Delay has benn changed into {}\n".format(Delay))
def checkTime():
	if(getTime()==timeTable[Nxti][0]):
		if(time.localtime().tm_sec==0):
			return timeTable[Nxti][1]
		else:
			# Delay=61
			pass
	return False
def init():
	log("Initializing...\n")
	mixer.pre_init(devicename="VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)")
	mixer.init()
	initTable()
	log("Initialized\n")


def main():
	while (1):
		if(Delay==Delay0):
			s = checkTime()
			if (s != False):
				Play(s+".wav")
				log(time.strftime("%Y %a %b %d %H:%M:%S ", time.localtime())+s+'\n')
				time.sleep(2)
		updateDelay()
		time.sleep(Delay)

def final():
	mixer.quit()
	
#######

init()
try:
	main()
except Exception as e:
	log(e)
final()
