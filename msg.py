from selenium import webdriver
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
import time

driver.get("https://web.whatsapp.com/")
time.sleep(10)
print("done sleeping")

name = input("write the name of user: ")
time.sleep(10)
user_message = input("write the messgae that u wanna send: ")
time.sleep(10)


search = driver.find_element_by_class_name("_1awRl copyable-text selectable-text")
search.send_keys(name)
print("bot has searched " + name)
time.sleep(1)
search.send_keys(keys.Keys.ENTER)
print("bot is inside the " + name + " chat")
time.sleep(1)
message = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
message.send_keys(user_message)
print("the bot is now writing message to " + name )
time.sleep(1)
message.send_keys(keys.Keys.ENTER)
print("congo bot sended the message to " + name)











