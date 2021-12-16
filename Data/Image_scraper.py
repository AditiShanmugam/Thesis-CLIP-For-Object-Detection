''' 
    Python script to scrape Google Images to generate a custom Dataset 
    Author: Aditi Shanmugam 
'''
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import time
import pandas as pd

wd = webdriver.Chrome(executable_path='') #Add path to webdriver (Chromedriver)

def downloader(keyword, img_path):
    
    #Loads Google Images.
    wd.get('https://images.google.com/imghp?hl=en&gl=ar&gws_rd=ssl')
    
    #Runs Image search for Keyword.
    search_box = wd.find_element_by_css_selector('input.gLFyf')
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.ENTER)

    #Scrolls down to the end of page.
    for i in range(2):
        wd.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)
        
    #Downloads Images.
    path = img_path
    soup = BeautifulSoup(wd.page_source, 'html.parser')
    img_tags = soup.find_all("img", class_="rg_i")
    time.sleep(2)

    count = 0
    for i in img_tags:
        try:
            urllib.request.urlretrieve(i['src'], path+keyword+str(count)+".jpg")
            count+=1
            print("Number of images downloaded = "+str(count),end='\r')
        except Exception as e:
            pass
          
       
keywords = [''] # Images/URLs to Scrape

path = '' #Add a path to create a folder to save images
os.mkdir(path, '') #Make directory at 'path' with the required name
for word in keywords:
    path_n = path +'/'+word+'/'
    os.mkdir(path_n)
    downloader(word, path_n)
    time.sleep(3)
wd.close()
