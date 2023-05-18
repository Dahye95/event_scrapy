import requests 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.maximize_window()

from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, "lxml")

import time

# 페이지 이동
url = 'http://gs25.gsretail.com/gscvs/ko/products/event-goods#;'
res = browser.get(url)
page_soup = BeautifulSoup(browser.page_source, 'html.parser')


# 마지막 페이지 구하기
last_page = browser.find_element(By.XPATH,'//*[@id="contents"]/div[2]/div[3]/div/div/div[1]/div/a[4]')
last_page.click()

## 스크롤
# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(2)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")

