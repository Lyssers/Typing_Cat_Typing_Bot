# TheTypingCatTypingBot
Very simple Python "typing bot" selenium scripts for websites TheTypingCat.com and 10FastFingers.com

Original is from:
!https://hackernoon.com/980-wpm-typing-bot-with-python-just-using-12-lines-of-code-ig2qj326c

![alt text](https://github.com/Lyssers/TheTypingCatTypingBot/blob/master/screenshot.png)

Updated by me to work on the latest version of the website at the time of code commits, modified to install browser extensions into the browser profile to get rid of ads/popups that may cause instability on lower-end hardware.

Also featuring a bot for the website 10fastfingers.

Note: For the 10fastfingers version, the script by default assumes you want to go as fast as possible, because it's fun to see, but 10fastfingers has a limited wordcount per test, and as it stands will time out due to inactivity because the bot finishes the test too fast, this is by design because while it's fun to see the bot go brrrr, cheating is bad and you should feel bad if you want to use it for that, so you will have to turn down the speed yourself to get a result that actually counts.

Requires Python3, Selenium and Geckodriver for Firefox.

