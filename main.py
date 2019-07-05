import re, glob, os, shutil, time
from pynput import keyboard

#GetCards() to most recent owned cards.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import strftime

lastCardSet = []
cards = []

try:
    cardFile = glob.glob(".\\record\\*")
    recentFile = max(cardFile, key=os.path.getctime)
    mostRecentFile = open(recentFile) 
    for line in mostRecentFile:
        lastCardSet.append(line)
except:
    print("First run")


def GetCards(lastCardSet, cards):
    url = 'https://www.saveeditonline.com/'

    configFile = open(".\\config.txt", "r")
    location = re.search('location:(.*)', configFile.read())[0]
    location = location[10:-1]
    configFile.close()

    listOfSaves = glob.glob(location+"\\*.sav")
    latestSave = max(listOfSaves, key=os.path.getctime)

    shutil.rmtree(".\\lastsave\\*", ignore_errors=True)
    shutil.copyfile(latestSave, ".\\lastsave\\latest.sav")

    saveToSend = os.path.abspath(".\\lastsave\\latest.sav")

    options = Options()
    options.set_headless(headless=True)
    driver = webdriver.Firefox(firefox_options=options)
    driver.get(url)
    submit = driver.find_element_by_id("fileupload")
    submit.send_keys(saveToSend)

    time.sleep(10)

    elements = driver.find_elements_by_tag_name('label')

    foundCards = False
    for element in elements:
        if element.text.find("GwentCard") == -1:
            continue
        else:
            cards.append('{0}'.format(element.text))
            foundCards = True

    driver.close()
    if (foundCards == False): 
        print("FAILED TO FIND CARDS. Please wait a few minutes before trying again.")
        return 
    currentTime = time.strftime("%Y%m%d%H%M")
    print(currentTime)
    cardsfile = open(".\\record\\cards"+currentTime+".txt", "x")
    for card in cards:
        if len(card)<25:
            print(card)
            cardsfile.write(card + "\n")
    cardsfile.close()
    CompareCards(lastCardSet, cards)
    lastCardSet = cards

    return lastCardSet

def CompareCards(lastCardSet, cards):

    lastCardSet = set(lastCardSet)
    cards = set(cards)
    newCards = cards - lastCardSet
    print(newCards)
    if not lastCardSet:
        return
    return

def on_press(key):
    try:
        if(key.char == '+'):
            print("Getting updated card list")
            GetCards(lastCardSet, cards)
            print("Finished!")
    except:
        return
    

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        print("Stopping...")
        return False

print("Gwent Card log started")
print("Press escape to stop")
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

