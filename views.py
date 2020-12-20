from selenium import webdriver
from selenium.webdriver.common import keys
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(ChromeDriverManager().install())

user = input("enter link: ")
time.sleep(5)
while True:
    driver.get(user)
    
    time.sleep(5)
    
