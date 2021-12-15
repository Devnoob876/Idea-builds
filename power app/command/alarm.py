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
			lib.close()
			week = str(input(">:"))
			result = p[week]
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
			lib.close()
			
			return p
	except Exception as e:
		print(e)

def add_alarm(path):
		isexist = os.path.exists(path)
		if isexist:
			lib = open(paths,'w')
			alarm = json.load(lib)
			lib.close()
			while True:
				print("Enter the time with am/pm in background")
				time = input(":>")
				
				weekday = datetime.datetime.now()
				weekday = str(weekday.strftime("%a"))
				if time != "":
					alarm[weekday]["time"] = time
					
					arr = ["am", "pm"]
					print("now enter am/pm")
					am_pm = str(input(":>"))
					if am_pm != "":
						if am_pm in arr:
							alarm[weekday]["day-night"] = am_pm
							lib = open(paths, 'w')
							json.dump(alarm, lib)
							lib.close()
							return "Added the time succesfully"
						else:
							print("add the right value")
							
					else:
						print("add the right value")
				else:
					print("add the right value")    





