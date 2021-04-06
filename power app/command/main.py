import time
import os
from playsound import playsound
import json

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
new = f"{BASE_DIR}\\assets\\"
os.chdir(new)

# oof hard coding stuff


def cl():
    
    print("please enter the problem:")
    while True:
        try:
            mat = str(input(":>"))
            if mat == "menu":
                menu()
            elif mat == "his_show":
                lib = open(new + "lib\\history.tmp","r")
                p = lib.read()
                print(p)
                lib.close()
            elif mat == "his_cls":
                lib = open(new + "lib\\history.tmp","w")
                lib.write("")
                lib.close()
            elif mat == "q":
                exit()
            else:
                result = str(eval(mat))
                lib = open(new + "lib\\history.tmp","a")
                lib.write(mat + "=" + result + "\n")
                lib.close()        
                print(result)
        except NameError:
            print(" please dont enter words instead of numbers!! ")
            time.sleep(2)
        except SyntaxError:
            print(" Syntax error ")
            time.sleep(2)



def clder():
    pass
def alr():
    pass
def wiki():
    pass
def pass_vault():
    pass


commands = {
        '-h': 'To get help runing apps type -h[app_short_name] e.g. -h[cl]',
        '-h[cl]': 'This app is calculator to start this type "cl", to exit type q instead of inserting math \n to get history of math results type -history instead of entering math ',
        '-h[clder]': 'type clder to start calander type "q" to exit type "n" to go to next moth',
        '-h[wiki]': 'type "wiki [question]" to get summary of your esteemed wiki result',
        '-h[alr]': 'type alr to open alarm; type set [time] to set alarm type ringtone to set ringtone ',
        '-h[p-v]': 'jjj',
        
        'cl': cl,
        'clder': clder,
        'wiki': wiki,
        'alr': alr 
        }


speeches = {
    
    'intro': "Welcome to Power app(cmd-version). \n This app is a combination of useful tools and other stuffs. To know all commands type: -h \n  To quit type -q",

    'tools': "In the [] brackets there are names in short form for opening it more easier and also get help easily \n 1. password vault[p-v] \n 2. calculator[cl] \n 3. calender[clder] \n 4. wikipedia result[wiki] \n 5. alarm-clock[alr] \n To get help type -h[small_form] e.g.: '-h[cl]' ",

    'alert': "Invalid command!! please type the currect command for the tools"    
        }
print(speeches.get('intro'))


def menu():
    while True:
        rply = input(":>")
    
        if rply in commands:        
            commands[rply]()
        elif rply == "cls":
            os.system("cls")
        elif rply == "q":
            exit()
        else:
            print(speeches.get('alert'))
            time.sleep(3)





menu()


