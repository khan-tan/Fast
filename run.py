#Author Mohammad sultani
import os, platform
try:
   import requests
except:
   os.system('pip2 install requests')

import requests
os.system("git pull") 
bit = platform.architecture()[0]
if bit == '64bit':
    from hik import menu
    menu()
elif bit == '32bit':
    from hik import menu
    menu()
