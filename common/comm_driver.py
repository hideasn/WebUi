# -*- coding: UTF-8 -*-
'''
作者: 梅兴和
日期: 2024/11/14 21:35
文件: comm_driver.py
项目: WebUi
描述: 
'''
from selenium import webdriver
from configs.config import Config
class CommonDriver:

    def get_driver(self, browser_type=Config.BROWSER_TYPE):
        if browser_type == "Chrome":
            self.driver = webdriver.Chrome()
        elif browser_type == "firefox":
            self.driver = webdriver.Firefox()

        self.driver.maximize_window()
        self.driver.set_page_load_timeout(20)
        return self.driver


