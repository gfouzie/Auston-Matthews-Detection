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



page_scroll_sleep = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(page_scroll_sleep)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
    #break #insert press load more
        try:
            element = driver.find_elements_by_class_name('mye4qd') #returns list
            element[0].click()
        except:
            break
    last_height = new_height


#scroll to the top
driver.execute_script("window.scrollTo(0,0)")

page_html = driver.page_source
pageSoup = bs4.BeautifulSoup(page_html, 'html.parser')
containers = pageSoup.findAll('div', {'class':"isv-r PNCib MSM1fd BUooTd"})

len_containers = len(containers)

print("Found", len_containers,"containers")

for i in range(1, len_containers+1):
    if i % 25 == 0:
        continue
    xPath = """//*[@id="islrg"]/div[1]/div[%s]"""%(i)

    #grab url of preview image
    previewImageXPath = """//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img"""%(i)
    previewImageElement = driver.find_element(By.XPATH, previewImageXPath)
    previewImageURL = previewImageElement.get_attribute("src")

    #click on image container
    driver.find_element(By.XPATH, xPath).click()

    #start a while true loop to wait until we the url instide the large image view is different from the previous one
    timeStarted = time.time()

    while(True):
        imageElement = driver.find_element(By.XPATH, """//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img""")
        imageURL = imageElement.get_attribute('src')

        if (imageURL != previewImageURL):
            break

        else:
            #make a timeout
            currentTime = time.time()

while(True):
    pass
    if (input("Enter any key to stop program: ")):
        break
    