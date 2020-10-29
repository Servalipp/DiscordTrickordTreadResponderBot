import time
import random
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print("Starting bot!")

print("Generating variables..")

#editable variables
trickMessage = "Open the door and greet them with h!trick"
treatMessage = "Open the door and greet them with h!treat"
maxCounts = 300
enableSpam = True
spamMessages = ["Wow I hope a bot spawns soon!",
                "Cant wait to get my next trinket"
                "I have to summon the bots with my messages",
                "*currently summoning bot*",
                "Give me a second im just summoning the bot right now",
                "Sorry for the spam guys, just waiting for the bot!",
                "wow this bot is sure taking its time",
                "...",
                "Ok when is this bot gonna come",
                "I am still waiting.",
                "Sooner or later this bot is gonna come",
                "sorry for the spam, just trying to summon the bot.",
                "Any day now...",
                "The bot is gonna come any day now",
                "I am just waiting for this bot but it isnt coming",
                "Ugh when is the bot gonna come."
                ]
#---------------

#dont edit these
counts = 0
#---------------

def reverseSpamMessages(x):
    return x[::-1]#reverses string

if enableSpam:
    print("Reversing messages because Selenium is confusing...")
    LIndex = 0
    for i in spamMessages:
        spamMessages[LIndex] = reverseSpamMessages(i)#assigns new backwards message to array
        LIndex += 1
        

options = Options()
#options.headless = True    #enable if you dont want the browser, but you cant sign in so it would break the bot, unless you automated that part aswell.  So probably dont enable actually
driver = webdriver.Firefox(options = options)
driver.implicitly_wait(1)
print("Driver Initiated")

def loop(trickMessage, treatMessage):
    everyInput = driver.find_element_by_tag_name("body")
    global counts
    global maxCounts
    global spamMessages
    if (trickMessage in driver.page_source):
        print("Bot found, h!trick type___________________")
        everyInput.send_keys("kcirt!h")#for some reason it types it in backwards so i do this
        time.sleep(1)
        everyInput.send_keys(Keys.ENTER)
    if (treatMessage in driver.page_source):
        print("Bot found, h!treat type___________________")
        everyInput.send_keys("taert!h")
        everyInput.send_keys(Keys.ENTER)
        time.sleep(1)
        
    
    if enableSpam:
        if (counts == maxCounts):
            everyInput.send_keys(spamMessages[random.randint(0, (len(spamMessages)-1))])
            everyInput.send_keys(Keys.ENTER)
            print("Sent spam")
            counts = 0
        else:
            counts += 1
            print(counts)


driver.get('https://discord.com/app')
input("Sign in, then go into the channel you want detected, and then hit enter")
print("Now Running...")

while True:
    loop(trickMessage, treatMessage)
    

