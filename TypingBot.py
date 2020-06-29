from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import re
import time
import platform
from pathlib import Path, PureWindowsPath
import os

#Enabling Extension Support:
#Check OS
#Change agv1sry4.default or q634iaqw.default-esr to your Firefox profile location name
if platform.system() == 'Windows':
       extensionPath = str(Path.home()) + str(PureWindowsPath('/AppData/Roaming/Mozilla/Firefox/Profiles/agv1sry4.default/extensions')) + os.sep
else:
    extensionPath =  "~/.mozilla/firefox/q634iaqw.default-esr/extensions/"
      
extensions = [
    "https-everywhere@eff.org.xpi", #HTTPS Everywhere
    "uBlock0@raymondhill.net.xpi", #Ublock Origin
    #"jid1-MnnxcxisBPnSXQ@jetpack.xpi" #Privacy Badger
    #Add Your Extension here
    ]

#Going on TypingCat
firefox = webdriver.Firefox()
firefox.get('https://thetypingcat.com/typing-speed-test/1m') #Change to 2m or 5m according to preference

#Installing Extensions
for extension in extensions:
   firefox.install_addon(extensionPath + extension, temporary=True)

#Sleep so the website can load and not slow us down
time.sleep(5) #Seconds

# Using javascript to get the typing content from the website and storing value in "string" variable
string = ''
for i in range(firefox.execute_script('return document.querySelectorAll(".line").length')):
	string += firefox.execute_script('return document.querySelectorAll(".line")['+str(i)+'].innerHTML')

#Regex to delete tags present inside the string
string = re.sub(r'<[^>]*>','',string) 

#Regex to replace the '⏎' symbol with a carriage return so enter it presses it for us
string = re.sub(r'\u23CE', '\\r',string) #Using \n will result in non-100% accuracy

#Type the text!
action = ActionChains(firefox)
action.send_keys(" ") #Since we have to press a key to start the game first.
action.send_keys(string)
action.perform()
