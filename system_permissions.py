# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
permission = android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("允许")')
try:
    permission.is_displayed()
    permission.click()
except:
    print("没有系统权限申请")

sleep(2)