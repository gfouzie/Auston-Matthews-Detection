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

#put search words into a list
searchWordsList = input("Please enter your search query with each word separated by one space: ").split()

#turn list into word+word+word format
searchWordsString = ""
for word in searchWordsList:
    searchWordsString+=word
    searchWordsString+="+"

searchWordsString = searchWordsString[:-1]
print(searchWordsString)

search_URL = "https://www.google.com/search?q="+searchWordsString+"&rlz=1C5CHFA_enCA952CA952&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjk1rGU-4z0AhWuQzABHVApBSMQ_AUoAnoECAEQBA&biw=1200&bih=899&dpr=2"
driver.get(search_URL)




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
            element = driver.find_elements(By.CLASS_NAME, 'mye4qd') #returns list
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
    print("Loaded image",i)

    xPath = """//*[@id="islrg"]/div[1]/div[%s]"""%(i)
    element = driver.find_element(By.XPATH, xPath)
    if element.get_attribute("class") == "isv-r PNCib MSM1fd BUooTd":
        element.click()

while(True):
    pass
    if (input("Enter any key to stop program: ")):
        break

    