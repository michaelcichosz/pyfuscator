#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
title = \
    """\
                __                           _                
               / _|                         | |               
 _ __   _   _ | |_  _   _  ___   ___   __ _ | |_   ___   _ __ 
| '_ \ | | | ||  _|| | | |/ __| / __| / _` || __| / _ \ | '__|
| |_) || |_| || |  | |_| |\__ \| (__ | (_| || |_ | (_) || |   
| .__/  \__, ||_|   \__,_||___/ \___| \__,_| \__| \___/ |_|   v.1.0
| |      __/ |                                                
|_|     |___/                                                 

obfuscating your python scripts...

(c)by Michael Cichosz
---------------------------------------------------------------------
contact:michaelcichosz(at)proton(dot)me
=====================================================================
"""
print(title)
#homedir = os.path.expanduser("~")
mydir = os.getcwd()


def print_menu():
    print((30 * '='+ ' OPTIONS '+ 30 * '='))
    print('1- Backwards encoding')
    print('2- Binary encoding')
    print('3- Ceasar encoding')
    print('4- char encryption (string)')
    print('5- char encryption (file)')
    print('6- char encryption - 0 (string)')
    print('7- char encryption - 0 (file)')
    print('8- Add EICAR Test Signature')
    print('9- Hex encoding')
    print('10- Create String as List')
    print('11- Binary to python')
    print('12- Add trashcode')
    print('13- Compile your script to .pyc')
    print('00- Exit')
    print(69 * '=')


loop = True

while loop:
    print_menu()
  
    choice = eval(input('Enter your choice [00-13]: '))
    
   
    if choice == 1:
        print('======================')
        print('= Backwards encoding =')
        print('======================')
        os.system('python3 ' + mydir + '/payloads/backwards.py')
        loop = False
    elif choice == 2:

        print('===================')
        print('= Binary encoding =')
        print('===================')
        os.system('python3 ' + mydir + '/payloads/binary.py')
        loop = False
    elif choice == 3:
        print('=====================')
        print('= Ceasar encryption =')
        print('=====================')
        os.system('python3 ' + mydir + '/payloads/ceasar.py')
        loop = False
    elif choice == 4:
        print('============================')
        print('= Char encryption (string) =')
        print('============================')
        os.system('python3 ' + mydir + '/payloads/chr.py')
        loop = False
    elif choice == 5:
        print('==========================')
        print('= Char encryption (file) =')
        print('==========================')
        os.system('python3 ' + mydir + '/payloads/chrfile.py')
        loop = False
    elif choice == 6:
        print('====================================')
        print('= Char encryption minus 0 (string) =')
        print('====================================')
        os.system('python3 ' + mydir + '/payloads/chrzero.py')
        loop = False
    elif choice == 7:
        print('==================================')
        print('= Char encryption minus 0 (file) =')
        print('==================================')
        os.system('python3 ' + mydir + '/payloads/chrfilezero.py')
        loop = False
    elif choice == 8:
        print('============================')
        print('= Add EICAR Test Signature =')
        print('============================')
        os.system('python3 ' + mydir + '/payloads/eicar.py')
        loop = False
    elif choice == 9:
        print('================')
        print('= Hex encoding =')
        print('================')
        os.system('python3 ' + mydir + '/payloads/hexread.py')
        loop = False
    elif choice == 10:
        print('==================')
        print('= String to List =')
        print('==================')
        os.system('python3 ' + mydir + '/payloads/listme.py')
        loop = False
    elif choice == 11:
        print('====================')
        print('= Binary to python =')
        print('====================')
        os.system('python3 ' + mydir + '/payloads/bin2hex.py')
        loop = False
    elif choice == 12:
        print('=================')
        print('= add Trashcode =')
        print('=================')
        os.system('python3 ' + mydir + '/payloads/trashcode.py')
        loop = False
    elif choice == 13:
        print('===============================')
        print('= Compile your script to .pyc =')
        print('===============================')
        os.system('python3 ' + mydir + '/payloads/createpyc.py')
        loop = False
    elif choice == 00:

        print('Quit - thanks for using Pyfuscator')
        loop = False
    else:

        eval(input('Wrong option selection. Enter any key to try again..'
             ))
