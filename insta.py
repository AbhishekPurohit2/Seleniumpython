
###   Selenium with Python  

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)

class Insta_demo:
    def insta_fun(self):
        driver.get("https://www.instagram.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//span[@class='_aacl _aaco _aacw _aad0 _aad7']").click()
        driver.find_element(By.XPATH, "//input[@name='emailOrPhone']").send_keys(9976543210)
        driver.find_element(By.XPATH, "//input[@name='fullName']").send_keys("Jack Sparrow")
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("jackywhd")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("9876@dafdadcds")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

instaobj = Insta_demo()
instaobj.insta_fun()


