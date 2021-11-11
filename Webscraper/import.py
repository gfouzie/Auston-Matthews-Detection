from logging import StreamHandler
from re import search
import bs4
from selenium import webdriver
import os 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


s=Service('/Users/gregfouzie/Desktop/Codermans/Drivers/chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()


search_URL = "https://www.google.com/search?q=auston+matthews&rlz=1C5CHFA_enCA952CA952&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjk1rGU-4z0AhWuQzABHVApBSMQ_AUoAnoECAEQBA&biw=1200&bih=899&dpr=2"
driver.get(search_URL)


#a = input("Waiting for user to start")

#scroll to the top
driver.execute_script("window.scrollTo(0,0);")

page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('div', {'class':"isv-r PNCib iPukc J3Tg1d"})

len_containers = len(containers)

print("Found", len_containers,"containers")

for i in range(1, len_containers+1):
    if i % 25 == 0:
        continue
    xPath = """//*[@id="islrg"]/div[1]/div[%s]"""%(i)
    driver.find_element(By.XPATH, xPath).click()