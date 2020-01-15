import time
import random
from selenium import webdriver

browser = webdriver.Chrome('/Users/abdulhalik/PycharmProjects/Selenium-EksiSozlukEntries/venv/chromedriver')
URL = "https://eksisozluk.com/fatih-sultan-mehmet--42269?p="

pageCount = 1
entryCount = 1
entries = []

# Generate random pages until 10 and browse them every 3 seconds -- 10 sayfa olana kadar 3 saniyede bir rastgele sayfa üret
while pageCount <= 10:
    randomPage = random.randint(1, 65)
    # Add random page number to end of the url
    # -- URL'in sonuna rastgele üretilmiş sayfa numarası ekle
    newUrl = URL + str(randomPage)
    browser.get(newUrl)
    # Get elements named on Content in that page
    # -- Content isimli elementleri sayfadan al
    # For multiple element use find_elements.... instead of find element....
    elements = browser.find_elements_by_css_selector('.content')
    # And push them into the Entry List for each page
    # -- Ve her birinin listeye ekle
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    pageCount += 1

# Print all entries in list
for entry in entries:
    print(str(entryCount) + "**************************************************")
    print(entry)
    entryCount += 1

browser.close()
