# -*- coding: UTF-8 -*-
'''
作者: 梅兴和
日期: 2024/11/14 21:57
文件: basePage.py
项目: WebUi
描述: 
'''
from comm_driver import CommonDriver

class BasePage:
    def __init__(self):
        self.driver = CommonDriver().get_driver()

    def open_url(self, url):
        self.driver.get(url)

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def input_text(self, locator, text, append_flag=False):
        if append_flag:
            pass
        else:
            self.get_element(locator).clear()
        self.get_element(locator).send_keys(text)

