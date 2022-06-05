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
from web.models import Seven


# selenium to open Chrome
driver = webdriver.Chrome()


# 페이지 열기
driver.get("https://www.7-eleven.co.kr/product/presentList.asp")
time.sleep(0.5)

# 더보기 클릭 - 상품 리스트 펼치기
while(True):
    try:
        driver.find_element(By.XPATH, '//li[@class="btn_more"]/a').click()
        time.sleep(0.5)
    except:
        break

# 상품 리스트
prodcuts = driver.find_elements(By.XPATH, '//ul[@id="listUl"]/li')
# 상품이 아닌 첫 번째 카드는 제외
for num, product in enumerate(prodcuts[1:]):
    # 첫 리스트 xpath
    if num < 13:
        li_path = 'div[@class="pic_product"]'
    # 이후 리스트 (더보기) xpath
    else:
        li_path = 'div[@class="pic_product"]/div[@class="pic_product"]'

    # 상품 정보 크롤링
    c_name = product.find_element(By.XPATH, f'{li_path}/div[@class="infowrap"]/div[@class="name"]').text
    c_price = product.find_element(By.XPATH, f'{li_path}/div[@class="infowrap"]/div[@class="price"]/span').text
    c_price = int(re.sub('[^0-9]', '', c_price))
    c_image = product.find_element(By.XPATH, f'{li_path}/img').get_attribute("src")

    # DB에 작성
    if not Seven.objects.filter(name = c_name):
        if __name__=='__main__':
            Seven(name=c_name, price=c_price, image=c_image).save()

driver.quit()