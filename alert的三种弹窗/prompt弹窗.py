# -*- coding: UTF-8 -*-
'''
作者: 梅兴和
日期: 2024/11/14 15:05
文件: confirm弹窗.py
项目: WebUi
描述: 
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/promptTest.htm")
driver.maximize_window()
sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[name=b1]").click()

sleep(2)
driver.switch_to.alert.send_keys("hello world")
sleep(2)
driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()
sleep(2)
driver.quit()
