import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "H:\python automations\chromedriver.exe"
print("Type total cases for total cases of COVID-19 ")
user = input('Which Country COVID cases you want to see? : ')
time.sleep(5)


driver = webdriver.Chrome(PATH)
driver.minimize_window()
driver.get("https://worldhealthorg.shinyapps.io/covid/")
time.sleep(3)


if user == "total cases":
    print("getting data from the server...")
    driver.get("https://worldhealthorg.shinyapps.io/covid/")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="closeModal"]').click()
    element = driver.find_element_by_xpath('//*[@id="tab-7605-1"]/div[1]/span[3]') # Get the element you want
    cases = element.text # Get the text within the element 
    cases = cases.split()[0]
    print("Total Cases Are: ",cases)
    exit()

   


driver.find_element_by_xpath('//*[@id="closeModal"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="tabs"]/li[2]/a').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="global_overview_subtabs"]/li[2]/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="render_case_death_table"]').click()

print('loading data from the server...')
time.sleep(10)

driver.find_element_by_xpath('//*[@id="DataTables_Table_0_filter"]/label/input').send_keys(user)
time.sleep(3)



hey = driver.find_element_by_xpath('//*[@id="DataTables_Table_0"]/tbody/tr/td[5]')
print("total cases in", user , "are:" , hey.text)
time.sleep(5)



























