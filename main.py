from selenium import webdriver
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
import time

maham = '_1hI5g _1XH7x _1VzZY'

driver.get("https://web.whatsapp.com/")
time.sleep(10)
print("done sleeping")

user = input()
time.sleep(12)


search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search.send_keys(user)
search.send_keys(keys.Keys.ENTER)

while True:
    state = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header')
    stateString = state.text
    if "online" in stateString:
        print(user +" is online ")
else:
    print(user + "is offline")

