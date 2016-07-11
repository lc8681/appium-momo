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

wd.find_element_by_id("maintab_layout_profile").click()   # 点击个人帧
wd.find_element_by_id("visitor_btn_login").click()    # 点击登录按钮

# wd.find_element_by_id("login_et_momoid").clear()  # 清除用户名

# username = raw_input("请输入用户名:")

# wd.find_element_by_id("login_et_momoid").send_keys(username)  # 输入用户名

password = raw_input("请输入密码:")

wd.find_element_by_id("login_et_pwd").send_keys(password)     # 输入密码
wd.find_element_by_id("btn_ok").click()    # 确定登录


try:
    wd.find_element_by_id("alertTitle").is_displayed()
    print("用户名或密码错误,请重试")
except:
    print("登录成功")
