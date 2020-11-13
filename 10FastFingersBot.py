from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import re
import time
import platform
from pathlib import Path, PureWindowsPath
import os
from selenium.webdriver.common.keys import Keys

#Enabling Extension Support:
#Change /q634iaqw.default-esr/ to your Firefox profile location
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

#Going on 10FastFingers
firefox = webdriver.Firefox()
firefox.get('https://10fastfingers.com/typing-test/english')

#Installing Extensions
#Sometimes extensions disappear when navigating to a different URL, so we do it after we go to the website
#This can cause some ads to still display
for extension in extensions:
    firefox.install_addon(extensionPath + extension, temporary=True)

#Sleep so the website can load and not slow us down loading
time.sleep(5) #Seconds

# Using javascript to get the typing content from the website and storing value in "string" variable
string = firefox.execute_script('return document.querySelectorAll(".highlight")[0].innerHTML')

#Type the word, then type space for every word.
while string != "":
	string = firefox.execute_script('return document.querySelectorAll(".highlight")[0].innerHTML')
	print(string)
	
#Type the text!
	action = ActionChains(firefox)
	action.send_keys(string)
	action.perform()
	action = ActionChains(firefox)
	action.send_keys(Keys.SPACE)
	action.perform()

