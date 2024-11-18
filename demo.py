# -*- coding: UTF-8 -*-
'''
作者: 梅兴和
日期: 2024/11/13 16:41
文件: demo.py
项目: WebUi
描述: 
'''

# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import Select
#
# driver = webdriver.Chrome()
# driver.get("http://sahitest.com/demo/selectTest.htm")
# driver.maximize_window()
# sleep(5)
# select = Select(driver.find_element(By.CSS_SELECTOR, '#s4Id'))
# # 防止反爬脚本
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": """
#     Object.defineProperty(navigator, 'webdriver', {
#       get: () => undefined
#     })
#   """
# })
#
# select.select_by_value('o1val')
# select.select_by_value('o3val')
# sleep(3)
# driver.quit()

# 声明一个空元组
empty_tuple = ()
#声明一个包含一个元素的元组
my_tuple = (1,)
#声明一个包含多个元素的元组
single_element_tuple = (1, "hello", 3)

# 2.使用tuple构造函数创建元组
char_tuple = tuple("hello")
print(char_tuple.count('l'))
print(char_tuple)

