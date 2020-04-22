import re
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Check if string has numbers
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

print("Starting Chrome...")

# Need this to start chrome correctly with Zotero Connector
chrome_options = Options()
chrome_options.add_extension('./macOS/extensions/zotero.crx')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./macOS/drivers/chromedriver')

# driver = webdriver.Chrome('./chromedriver')
test_url = "https://scholar.google.com/scholar?hl=en&start=0&as_sdt=0%2C5&q=%28intitle%3Arobot%29+AND+%28intitle%3Apower+OR+intitle%3Agreen+OR+intitle%3Aenergy+OR+intitle%3Abattery%29+AND+software&btnG="
driver.get(test_url)

# Find how many results are present.
# gs_ab_mdw
found = None
elements = driver.find_elements_by_class_name('gs_ab_mdw') # Make this classname future proof (needs to be able to change)
for elem in elements:
    if hasNumbers(elem.text):
        found = elem

nr_of_records = re.findall(r'\d+', found.text)[0]
print("number of records: ", nr_of_records)

## PROGRAM CONTINUES, MAKE COHERENT

print("Chrome started... waiting 2s...")

pos = None
time.sleep(2)
while pos is None:
    pos = pyautogui.locateOnScreen("./macOS/images/zotero_tree_source.png")

print("Succesful")
# ONLY FOR MACBOOK ( SCREEN BUG )
click_x = pos[0] / 2 + (pos[2] / 2) / 2
click_y = pos[1] / 2 + (pos[3] / 2) / 2
 
pyautogui.click(x=click_x,y=click_y,clicks=1,interval=0.0,button="left")
time.sleep(1)

pos = None
while pos is None:
    pos = pyautogui.locateOnScreen("./macOS/images/zotero_select_all.png")

# ONLY FOR MACBOOK ( SCREEN BUG )
click_x = pos[0] / 2 + (pos[2] / 2) / 2
click_y = pos[1] / 2 + (pos[3] / 2) / 2

pyautogui.click(x=click_x,y=click_y,clicks=1,interval=0.0,button="left")

time.sleep(2)

driver.quit()