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
desired_caps['deviceName'] = '860BCML225ZG'  # adb devices查到的设备名
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['automationName'] = 'Selendroid'  # Selendroid模式
desired_caps['appPackage'] = 'com.immomo.momo'  # 被测App的包名
desired_caps['appActivity'] = 'com.immomo.momo.android.activity.WelcomeActivity'  # 启动时的Activity
self = webdriver.Remote('http://localhost:4723/self/hub', desired_caps)