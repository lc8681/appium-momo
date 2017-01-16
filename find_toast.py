# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_toast(self, toast_message):
        # 判断toast信息
        try:
            android_caps.self = WebDriverWait(self.driver, 10)\
                .until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, toast_message)))
            return True
        except:
            return False