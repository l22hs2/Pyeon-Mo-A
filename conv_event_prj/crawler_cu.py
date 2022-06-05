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
from web.models import Cu


# selenium to open Chrome
driver = webdriver.Chrome()


# 페이지 열기
driver.get("https://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N")

time.sleep(1)
driver.find_element(By.XPATH, '//li[@class="eventInfo_02 "]/a').click()
time.sleep(2)

# while(True):
#     try:
#         driver.find_element(By.XPATH, '//div[@class="prodListBtn-w"]').click()
#         time.sleep(3)
#     except:
#         break

while(True):
    try:
        time.sleep(1)
        if driver.find_element(By.XPATH, '//div[@class="prodListBtn-w"]'):
            driver.execute_script('nextPage(1);')
    except:
        break



prodcuts_ul = driver.find_elements(By.XPATH, '//div[@class="prodListWrap"]/ul')

for products in prodcuts_ul:
    prodcut_li = products.find_elements(By.XPATH, 'li')
    for product in prodcut_li:
        c_name = product.find_element(By.XPATH, 'a/div[@class="prod_wrap"]/div[@class="prod_text"]/div[@class="name"]/p').text
        c_price = product.find_element(By.XPATH, 'a/div[@class="prod_wrap"]/div[@class="prod_text"]/div[@class="price"]/strong').text
        c_price = int(re.sub('[^0-9]', '', c_price))
        c_image = product.find_element(By.XPATH, 'a/div[@class="prod_wrap"]/div[@class="prod_img"]/img').get_attribute("src")

        if not Cu.objects.filter(name = c_name):
            if __name__=='__main__':
                Cu(name=c_name, price=c_price, image=c_image).save()