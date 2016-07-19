# -*- coding: utf-8 -*-
# python学习，加油！

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selendroid_demo

def find_toast(self, toast_message):
        # 判断toast信息
        try:
            selendroid_demo.wd = WebDriverWait(self.driver, 10)\
                .until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, toast_message)))
            return True
        except:
            return False