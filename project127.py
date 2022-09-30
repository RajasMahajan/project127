from  selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("/path/to/chromedriver")
browser.get(START_URL)
time.sleep(10)

Soup = BeautifulSoup(browser.page_source,"html.parser")
for tr_tag in Soup.find_all("tr",attrs = {"class": "headerSort"}):
        tr_tags = tr_tag.find_all("tr")
temp_list = []
for index,tr_tag in enumerate(tr_tags):
    if index == 0:
        temp_list.append(tr_tag.find_all("a")[0].content[0])
    else:
        try:
                temp_list.append(tr_tag.content[0])
        except:
                temp_list.append("")