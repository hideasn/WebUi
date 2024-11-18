# -*- coding: UTF-8 -*-
'''
作者: 梅兴和
日期: 2024/11/14 14:49
文件: alert弹窗.py
项目: WebUi
描述: 
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/alertTest.htm")
driver.maximize_window()
sleep(5)
driver.find_element(By.CSS_SELECTOR, "input[name=b1]").click()

sleep(2)
driver.switch_to.alert.accept()
sleep(2)
driver.quit()
