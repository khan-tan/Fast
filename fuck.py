# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Mar  1 2022, 15:44:46) 
# [GCC Android (7714059, based on r416183c1) Clang 12.0.8 (https://android.google
# Warning: this version of Python has problems handling the Python 3 byte type in constants properly.

# Embedded file name: <Jutt Badshah>
# Compiled at: 2022-02-17 23:01:11
try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests, os, time, uuid, requests
    from multiprocessing.pool import ThreadPool
    os.system('clear')
    os.system('termux-setup-storage')
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install lolcat')

os.system('clear')
from requests.exceptions import ConnectionError
os.system('git pull')
logo = '                                      \n  .____/\ .______  .______  ._____.___ .______ /n :   /  \:      \ : __   \ :         |:      \ |.  ___/|   .   ||  \____||   \  /  ||   .   ||     \ |   :   ||   :  \ |   |\/   ||   :   ||      \|___|   ||   |___\|___| |   ||___|   ||___\  /    |___||___|         |___|    |___|     \/                                \n\n\x1b[1;95m-----------------------------------------------  \n\x1b[1;37m[*] AUTHOR   :\x1b[1;97m KARMA DAVID\n\x1b[1;37m[*] WHATSAPP :\x1b[1;37m +2348110044418\n\x1b[1;37m(*)TOOl TYPE : BYPASSED \n\x1b[1;37m[*] FACEBOOK : KARMA DAVID\n\x1b[1;37m[*] WARNING  : IF YOURE BAD AM YOUR DAD \n\x1b[1;37m-----------------------------------------------                       \n       SUPREME BOT USERS\n\x1b[1;91m-----------------------------------------------\n \n'

def main_apv():
    imt = '~~KARMA=='
    os.system('clear')
    print logo
    try:
        key1 = open('/sdcard/Pictures/.1.txt', 'r').read()
    except IOError:
        os.system('clear')
        print logo
        print '           THIS IS YOUR KEY BITCH'
        print ''
        myid = uuid.uuid4().hex[:18]
        print '          YOUR KEY : ' + myid + imt
        kok = open('/sdcard/Pictures/.1.txt', 'w')
        kok.write(myid + imt)
        kok.close()
        print ''
        print ''
        raw_input('      Copy Key And Press Enter For Approvel Your Key ')
        os.system('xdg-open https://wa.me/+2348110044418')

    r1 = requests.get('https://raw.githubusercontent.com/Karma-kh3n/Bypass/main/Karma.txt').text
    if key1 in r1:
        main()
    else:
        os.system('clear')
        print logo
        print '          THIS IS YOUR KEY BRO'
        print ''
        print '          YOUR KEY : ' + key1
        print ''
        raw_input('      Copy Key And Press Enter For Approvel Your Key ')
        os.system('xdg-open https://wa.me/+2348110044418')


def main():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;92m[1] \x1b[1;97mSTART CLONING FROM\x1b[1;32m [JAMES] '
    print ''
    print '\x1b[1;92m[2] \x1b[1;97mSTART CLONING FROM\x1b[1;32m [ADF] '
    print ''
    print '\x1b[1;92m[3] \x1b[1;97mSTART CLONING FROM\x1b[1;32m [JUTT] '
    print ''
    print '\x1b[1;92m[4] \x1b[1;97mSTART DUMP IDZ FOR\x1b[1;32m [CLONING]'
    print ''
    print '\x1b[1;92m[w] \x1b[1;97mFOR NEED ANY HELP\x1b[1;32m WHATSAPP ME'
    print ''
    print '\x1b[1;91m[0] \x1b[1;97mEXIT TOLLS'
    print ''
    print '\x1b[1;37m-----------------------------------------------'
    print ' FOR NEED ANY HELP CLICK w AND \x1b[1;32mWHATSAPP ME'
    print '\x1b[1;37m-----------------------------------------------'
    print ''
    main_select()


def main_select():
    King = raw_input('\x1b[1;97m[!] Choose Opition ---> \x1b[1;91m ')
    if King == '1':
        os.system('python Prohack.py')
        main()
    if King == '2':
        os.system('python Adf.py')
        main()
    if King == '3':
        os.system('python2 Juttbrand.py')
        main()
    elif King == '4':
        os.system('git clone https://github.com/THE-DEMON-ANNOS/Extract')
        os.system('cd Extract && chmod +x extract && ./extract')
        main()
    elif King == '0':
        os.system('exit')
    elif King == 'w' or King == 'W':
        os.system('xdg-open https://wa.me/+2348110044418')
        main()
    else:
        print ('[!] Please select a valid option').center(50)
        time.sleep(1)
        main()


if __name__ == '__main__':
    main_apv()
# okay decompiling out.pyc
