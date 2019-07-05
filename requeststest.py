import re
import glob
import shutil
import os

url = 'https://www.saveeditonline.com/'

config_file = open(".\\config.txt", "r")
location = re.search('location:(.*)', config_file.read())[0]
location = location[10:-1]
config_file.close()

list_of_saves = glob.glob(location+"\\*.sav")
latest_save = max(list_of_saves, key=os.path.getctime)

shutil.rmtree(".\\lastsave\\*", ignore_errors=True)
shutil.copyfile(latest_save, ".\\lastsave\\latest.sav")

save_to_send = os.path.abspath(".\\lastsave\\latest.sav")
