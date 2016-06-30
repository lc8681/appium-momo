# -*- coding: utf-8 -*-
# python学习，加油！
import sys
import os
from selenium import webdriver
from appium import webdriver
import time
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
time.sleep(3)

desired_caps = {}
desired_caps['deviceName'] = '860BCML225ZG'  #adb devices查到的设备名
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['appPackage'] = 'com.immomo.momo'  #被测App的包名
desired_caps['appActivity'] = 'com.immomo.momo.android.activity.WelcomeActivity' #启动时的Activity
wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)