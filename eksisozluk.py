import time
from selenium import webdriver

browser = webdriver.Chrome('/Users/abdulhalik/PycharmProjects/Selenium-EksiSozlukEntries/venv/chromedriver')
url = "https://eksisozluk.com/sakir-kocabas--161122"
browser.get(url);
time.sleep(10)
browser.close()