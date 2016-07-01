# -*- coding: utf-8 -*-
# python学习，加油！
import sys
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
desired_caps['appPackage'] = 'com.immomo.momo'  # 被测App的包名
desired_caps['appActivity'] = 'com.immomo.momo.android.activity.WelcomeActivity' # 启动时的Activity
wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
wd.implicitly_wait(10)   # 等待元素10s
sleep(5)
wd.find_element_by_id("maintab_layout_profile").click()   # 点击个人帧
wd.find_element_by_id("visitor_btn_login").click()    # 点击登录按钮
wd.find_element_by_id("login_et_momoid").clear()
wd.find_element_by_id("login_et_momoid").send_keys("219530396")   # 输入用户名
wd.find_element_by_id("login_et_pwd").send_keys("momo1234")     # 输入密码
wd.find_element_by_id("btn_ok").click()

# <------------- 以 下 为 登 录 后 ------------->
wd.find_element_by_id("maintab_layout_profile").click()
wd.swipe(200,500,100,500)
wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ExpandableListView[1]/android.widget.LinearLayout[12]/android.widget.LinearLayout[1]").click()
wd.find_element_by_id("setting_layout_msg_notice").click()

soundcheckbox = WebDriverWait(wd, 5, 0.5).until(
    EC.element_selection_state_to_be(wd.find_element_by_id("setting_cb_sound"))
)
print soundcheckbox
#if soundcheckbox = "true"
#wd.find_element_by_id("setting_cb_sound").click()  #点击声音
wd.quit()
