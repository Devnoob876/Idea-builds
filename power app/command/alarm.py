import os

import time
import datetime
import json





def search_alarms(paths):
	try:
		
		isexist = os.path.exists(paths)
		if isexist:
			
			lib = open(paths,'r')
			alarm = json.load(lib)
			p = alarm["alarms"]
			result = json.dumps(p)
			return result
			
		else:
			print("sorry your alarm app was corrupted")
	except Exception as e:
		print(e)
		
			
def today_alarm(paths):
	try:
		
		isexist = os.path.exists(paths)
		if isexist:
			lib = open(paths,'r')
			alarm = json.load(lib)
			today = datetime.datetime.now()
			today = str(today.strftime("%a"))
			p = alarm["alarms"][today]
			
			return p
	except Exception as e:
		print(e)
		
def add_alarm(path):
	



