import os
import sys

import psutil
from clint.textui import colored
from pyfiglet import Figlet


### Colors
def warning(text):
    warning = colored.yellow(text)
    return warning

def success(text):
    success = colored.green(text)
    return success

def inputcolor(text):
    inputcolor = colored.cyan(text)
    return inputcolor

def tect(a,b,c):
    if a+0.5*c/b>5:
       horse='优质队友'
    elif a+0.5*c/b>2:
        horse = '中等队友'
    else:
        horse = '不推荐成为队友'
    return horse


# 检测是哪个功能在运行
def ProcessRunning(ProcessName):
    for proc in psutil.process_iter():
        try:
            if ProcessName in proc.name():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


def lolrunning():
    if ProcessRunning("LeagueClient"):
       print(success("[+] ") + "LoL are Running!")
    else:
        print(warning("[!] ") + "LoL are not running!")
        sys.exit()
#检测lol是否在运行

########## Change Status  ##########


def checkfileexist():
    file = "status.txt"
    if os.path.exists(file) == False:
        with open(file, mode='a'): pass
        print(warning("[!] ") + file + " not found! Creating the file...")
        sys.exit()

def checkfileempy():
    file = "status.txt"
    if os.stat(file).st_size == 0:
        print(warning("[!] ") + "The file is empty! Canceling... ")
        sys.exit()


########## 菜单界面  ##########

def welcome(text):
    result = Figlet()
    return colored.cyan(result.renderText(text))

def extract_element_from_json(obj, path):
    '''
    输入关键字，就可以将关键字的值信息存放在列表中并输出
    如果关键字是对象名，则返回的对象字典信息到列表中
    如果关键字是列表名，则返回的列表信息到列表中（返回双重列表）
    '''
#混子代码完全没用已经删除了

def Menu():
    if os.name == 'nt':
         os.system("cls")
    else:
        os.system("clear")
    print(welcome("lol welcome"))
    print("""
--== Menu ==--
 [1] Icon Changer
 [2] Background Changer
 [3] Rank Changer
 [4] Status Changer
 [5] AutoAccept
 [6] Change Locale
 [7] Offline Status
 [8] Online Status
 [9] More Bots In Practice Tool
 [10] Custom Request
 [12] Team BP
 [13] Person BP
 [0] Exit
--==========--
    """)