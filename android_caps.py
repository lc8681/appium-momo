# -*- coding: utf-8 -*-
# python学习，加油！
import os
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

desired_caps = []
desired_caps['deviceName'] = '850ABM3SRGJF'  # adb devices查到的设备名
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['appPackage'] = 'com.immomo.momo'  # 被测App的包名
desired_caps['appActivity'] = 'com.immomo.momo.android.activity.WelcomeActivity'  # 启动时的Activity
# desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

wd.implicitly_wait(5)   # 等待元素5s