# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:40:53 2021

@author: NoobyPro/Tahmid
"""

import os
import argparse
#import colorama
import win32api as win


main_dir = ""
print(print("welcome to expy an console based file explorer \n type -h"))
err = 0




def main():
	main_dir = os.getcwd()
	while err < 1:
		user = input(":>")
		if user == "-h":
			pass
		elif user == "ls drive":
		    drives = win.GetLogicalDriveStrings()
		    drives = drives.split('\000')[:-1]
		    print(drives)
		elif "goto" in user:
			going_to_drive(user, main_dir)
            
def exist_dir(obj, old):
	while err < 1:
		user = input(":>") 
		if user in obj:
			cwd = os.getcwd()
			path = str(f"{cwd}\\{user}")
			os.chdir(path)
			going_to_drive(path,old)
			path = ""
		elif "close" in user:
			os.chdir(old)
			print(f"explorer closed current directory {old}")
			main()
		elif ".." in user:
			cwd = os.getcwd()
			path = os.path.dirname(cwd)
			going_to_drive(path, old)


def going_to_drive(direname, old):
	if "goto " in direname:
		direname = direname[5:]
		print(direname)

		if os.path.exists(direname):
			os.chdir(direname)
			print("showing all files of ", direname)
			files = os.listdir()
			for f in files:
				print("\n")
				print(f)
			exist_dir(files, old)
		else:
			print("That is not a valid directory!")
			main()


	elif "goto " not in direname:
		if os.path.exists(direname):
			os.chdir(direname)
			print("showing all files of ", direname)
			files = os.listdir()
			for f in files:
				print("\n")
				print(f)
				
			exist_dir(files, old)

if __name__ == "__main__":
	main()