# -*- coding: UTF-8 -*-
'''
作者: 梅兴和
日期: 2024/11/14 15:31
文件: 文件上传.py
项目: WebUi
描述: 
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.set_window_size(600, 600)
sleep(2)