import logging
from selenium import webdriver
from selenium.webdriver.common import keys
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
#driver = webdriver.Chrome(ChromeDriverManager().install())
#instagram = "https://www.instagram.com/"
facebook = "https://web.facebook.com/"
#link = input("enter link : ")
#time.sleep(10)
#print("done sleeping now starting the program")

#driver.get(instagram)
#driver.get(instagram)
#time.sleep(1)
#time.sleep(1)
#username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
#username.send_keys("anime_freak.69")
#time.sleep(1)
#
#password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
#password.send_keys("rahmani922")
#time.sleep(1)
#

#login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
#login.click()
#time.sleep(5)
#

#pop = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
#pop.click()
#time.sleep(5)
#
#not_now = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
#not_now.click()
#time.sleep(2)

#messages = driver.find_element_by_class_name('xWeGp')
#messages.click()
#time.sleep(5)
#first = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[2]/a/div')
#print("group found")
#first.click()
#print("group clicked")
#time.sleep(5)

#message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
#print("message box found")
#message_box.click()
#time.sleep(1)
#print("clicked!")
#message_box.send_keys(link)
#time.sleep(1)
#message_box.send_keys(keys.Keys.ENTER)
#time.sleep(3)

#secand_group = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div/div/div[2]/div')
#print("group found")
#secand_group.click()
#print("group clicked")
#time.sleep(5)
#message_box2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
#print("message box found")
#message_box2.click()
#time.sleep(1)
#print("clicked!")
#message_box2.send_keys(link)
#time.sleep(1)
#message_box2.send_keys(keys.Keys.ENTER)

#driver.quit()
#time.sleep(2)

driver2 = webdriver.Chrome(ChromeDriverManager().install())

driver2.get(facebook)
time.sleep(2)

email = driver2.find_element_by_xpath('//*[@id="email"]')
email.send_keys("hassan.rahmani922@gmail.com")
time.sleep(1)
password1 = driver2.find_element_by_xpath('//*[@id="pass"]')
password1.send_keys("gamebox8")
time.sleep(1)
login1 = driver2.find_element_by_xpath('//*[@id="u_0_b"]')
login1.click() 
time.sleep(3)

groups = driver2.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[3]/div/div[1]/div[1]/ul/li[4]/span/div/a')
groups.click()
time.sleep(2)
group_search = driver2.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/label/input')
group_search.send_keys("python")
time.sleep(1)
group_search.send_keys(keys.Keys.ENTER)
time.sleep(3)

python_group = driver2.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/h3/span/span/div/a/span')

print("group found!")
python_group.click()
print("group clicked!")
time.sleep(3)
post = driver2.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div')
post.click()
time.sleep(1)
post.send_keys("hey! i am making a share social media bot that will share my latest video link to my all social media accounts and thsi messgae is also typed by him wanna see how i made it")
time.sleep(4)




