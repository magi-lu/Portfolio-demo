#自動登入 搜尋 下載twitter圖片
from ast import keyword
import os
from tkinter import Widget
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import wget

#輸入瀏覽器驅動路徑   ↓↓↓↓↓↓↓↓↓↓
PATH = "E:/D/1/webdriver/msedgedriver.exe"
driver = webdriver.Edge(PATH)
driver.get("https://twitter.com/i/flow/login") 

time.sleep(5)
username = driver.find_element_by_css_selector('input[autocomplete="username"]')
username.clear()
#輸入twiter帳號      ↓↓↓↓↓↓↓↓↓↓↓
username.send_keys('此處輸入帳號')
print('輸入帳號完成')
time.sleep(3)
loadnext2 = driver.find_element_by_css_selector('div[style="color: rgb(255, 255, 255);"]')
loadnext2.click()
print("下一步")
time.sleep(3)

password = driver.find_element_by_name('password')
password.clear
#輸入twitter密碼    ↓↓↓↓↓↓↓↓↓↓↓
password.send_keys('此處輸入密碼')
print('輸入密碼完成')
time.sleep(2)
loadnext3 = driver.find_element_by_css_selector('div[style="color: rgb(255, 255, 255);"]')
loadnext3.click()
print('登入成功')
time.sleep(5)
search = driver.find_element_by_css_selector('input[placeholder="搜尋 Twitter"]')
#輸入要搜尋的關鍵字 
keyword = "#笹の絵"

search.send_keys(keyword)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(5)
print("搜尋成功")

#網頁往下拉 迴圈
for i in range (5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

#讀取 下載圖片
imgs = driver.find_elements_by_css_selector( 'img[alt="圖片"]')
imgfolder = os.path.join(keyword)
os.mkdir(imgfolder)
count = 0
for img in imgs:
    save_as = os.path.join(imgfolder, keyword + str(count) + '.jpg')
    #print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"), save_as)
    count += 1