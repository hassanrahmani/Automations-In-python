from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
how = r"chromedriver.dmg"

url = 'https://www.youtube.com/channel/UCvwDvEh9i7Ge8bs_tw6nrrA/videos'

driver = webdriver.Chrome(executable_path=how)
driver.get(url)
time.sleep(2)

sort = driver.find_element_by_xpath('//*[@id="icon-label"]').click()
time.sleep(1)
older = driver.find_element_by_xpath('//*[@id="menu"]/a[2]/tp-yt-paper-item/tp-yt-paper-item-body/div[1]').click()
time.sleep(2)

video = driver.find_element_by_xpath('//*[@id="video-title"]')
lol = video.get_attribute('href')

driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
time.sleep(2)
driver.get('https://yt1s.com/en5')
time.sleep(4)
space = driver.find_element_by_xpath('//*[@id="s_input"]')
print('input field found')
space.send_keys(lol)
print("url pasted")
time.sleep(3)
print('clickig covert..')
driver.find_element_by_xpath('//*[@id="search-form"]/button').click()
time.sleep(5)
print('get link button')
driver.find_element_by_xpath('//*[@id="btn-action"]').click()
time.sleep(5)
print("download button")
driver.find_element_by_xpath('//*[@id="asuccess"]').click()
print('downlpoading video1.....')
time.sleep(5)
print("starting to download next video...")
#2nd video
driver = webdriver.Chrome(executable_path=how)
driver.get(url)
print('clicking sort button')
sort = driver.find_element_by_xpath('//*[@id="icon-label"]').click()
time.sleep(1)
print('clicking oldest video')
older = driver.find_element_by_xpath('//*[@id="menu"]/a[2]/tp-yt-paper-item/tp-yt-paper-item-body/div[1]').click()
time.sleep(2)

print('clicking the video>>>')
video2 = driver.find_element_by_xpath('//*[@id="items"]/ytd-grid-video-renderer[2]').click()
time.sleep(3)
print('getting url of video<><>')
hello = driver.current_url



driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
time.sleep(2)
driver.get('https://yt1s.com/en5')
time.sleep(4)
space = driver.find_element_by_xpath('//*[@id="s_input"]')
space.send_keys(hello)
time.sleep(3)

driver.find_element_by_xpath('//*[@id="search-form"]/button').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="btn-action"]').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="asuccess"]').click()
time.sleep(4)

#video3
print("starting to download next video...")
print('opeaning chrome')
driver = webdriver.Chrome(executable_path=how)
driver.get(url)
time.sleep(2)
print("copy video link")
uf = driver.find_element_by_xpath('//*[@id="video-title"]')
lmao = uf.get_attribute('href')
time.sleep(2)
print('new tab')
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
time.sleep(3)
driver.get('https://yt1s.com/en5')
time.sleep(4)
space = driver.find_element_by_xpath('//*[@id="s_input"]')
space.send_keys(lmao)
time.sleep(3)

driver.find_element_by_xpath('//*[@id="search-form"]/button').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="btn-action"]').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="asuccess"]').click()
time.sleep(5)
print('done downloding video')

print('*******lets uplaod them***********')
print("you have to goto desktop when its says 'goto desktop' ")





