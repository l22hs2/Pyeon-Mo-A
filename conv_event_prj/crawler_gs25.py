import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import re

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conv_event_prj.settings')
import django
django.setup()
from web.models import Product


# selenium to open Chrome
driver = webdriver.Chrome()


# 페이지 열기
driver.get("http://gs25.gsretail.com/gscvs/ko/products/event-goods")


event = driver.find_elements(By.XPATH, '//div[@class="eventtab"]/div')
one_plus_one = event[0] # 1+1 상품 리스트
two_plus_one = event[1] # 2+1 상품 리스트


# 마지막 페이지 수 확인
pages = driver.find_element(By.XPATH, '//div[@class="paging"]/a[@class="next2"]').get_attribute("onclick")
pages = int(re.sub('[^0-9]', '', pages)) # 숫자만 추출

# 페이지 수 만큼 반복
for page in range(pages):

    # 상품 목록
    opo = one_plus_one.find_elements(By.XPATH, 'ul[@class="prod_list"]/li')

    # 상품 정보
    for product in opo:
        c_name = product.find_element(By.XPATH, 'div[@class="prod_box"]/p[@class="tit"]').text
        c_price = product.find_element(By.XPATH, 'div[@class="prod_box"]/p[@class="price"]/span').text
        c_price = int(re.sub('[^0-9]', '', c_price)) # 숫자만 추출
        try:
            c_image = product.find_element(By.XPATH, 'div[@class="prod_box"]/p[@class="img"]/img').get_attribute("src")
        except:
            c_image = "..."

        today = datetime.date.today()

        # DB 작성
        # 이미 상품이 있으면
        if Product.objects.filter(name = c_name):
            p = Product.objects.get(name = c_name)
            if p.store == "GS25":
                p.created_at = today
                p.save()
            
        # 상품이 없으면
        else:
            # 메인 함수 선언
            if __name__=='__main__':
                Product(store="GS25", name=c_name, price=c_price, image=c_image, created_at=today).save()


    # 다음 페이지로 이동
    if page != pages:
        driver.find_element(By.XPATH, '//div[@class="paging"]/a[@class="next"]').click()
        time.sleep(1)

driver.quit()