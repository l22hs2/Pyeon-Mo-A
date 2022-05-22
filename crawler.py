from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import csv
import re

# writer = csv.writer(open("GS25.csv", "w", encoding="utf-8-sig", newline=""))
# title = ["network", "plan", "name", "charge", "code"]
# writer.writerow(title)

# selenium to open Chrome
driver = webdriver.Chrome()

# 페이지 열기
driver.get("http://gs25.gsretail.com/gscvs/ko/products/event-goods")


event = driver.find_elements(By.XPATH, '//div[@class="eventtab"]/div')
one_plus_one = event[0] # 1+1 상품 목록
two_plus_one = event[1] # 2+1 상품 목록


# 마지막 페이지 수 확인
pages = driver.find_element(By.XPATH, '//div[@class="paging"]/a[@class="next2"]').get_attribute("onclick")
pages = int(re.sub('[^0-9]', '', pages)) # 숫자만 추출

for page in range(pages):

    # 상품 목록
    opo = one_plus_one.find_elements(By.XPATH, 'ul[@class="prod_list"]/li')

    # 상품 정보
    for product in opo:
        title = product.find_element(By.XPATH, 'div[@class="prod_box"]/p[@class="tit"]').text
        price = product.find_element(By.XPATH, 'div[@class="prod_box"]/p[@class="price"]/span').text
        
        print(f"{title} - {price}")

    # 다음 페이지로 이동
    if page != pages:
        driver.find_element(By.XPATH, '//div[@class="paging"]/a[@class="next"]').click()
        time.sleep(0.5)
