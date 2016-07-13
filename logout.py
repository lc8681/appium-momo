# -*- coding: utf-8 -*-
# python学习，加油！

import sys
from sys import argv
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
desired_caps = {}
desired_caps['deviceName'] = '850ABM3SRGJF'  # adb devices查到的设备名
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['appPackage'] = 'com.immomo.momo'  # 被测App的包名
desired_caps['appActivity'] = 'com.immomo.momo.android.activity.WelcomeActivity'  # 启动时的Activity
wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
wd.implicitly_wait(10)   # 等待元素10s

sleep(5)
wd.find_element_by_id("maintab_layout_profile").click()  # 点击个人帧
wd.swipe(start_x=534, start_y=1534, end_x=534, end_y=415, duration=None)  # 向下滑动

sleep(3)
wd.find_element_by_android_uiautomator('new UiSelector().text("设置")').click()  # 按text查找

sleep(3)
wd.find_element_by_id("setting_layout_logout").click()   # 点击"退出陌陌"

sleep(3)
wd.find_element_by_android_uiautomator('new UiSelector().text("退出当前帐号")').click()
wd.find_element_by_id("button1").click()

sleep(3)
try:
    logout = wd.find_element_by_id("btn_ok").is_enabled()
    print("退出账号成功")

except:
    print("退出账号失败")

sleep(10)
wd.quit()



