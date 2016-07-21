# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
from random import choice
from appium.webdriver.common.touch_action import TouchAction

action = TouchAction(android_caps.wd)
android_caps.wd.find_element_by_id("maintab_layout_contact").click()
android_caps.wd.find_element_by_id("friend_action_search").click()
android_caps.wd.find_element_by_id("toolbar_search_edittext").send_keys("220850234")
try:
    android_caps.wd.find_element_by_id("section_title").click()
except:
    print("没有搜素到用户")
android_caps.wd.find_element_by_id("profile_layout_start_chat").click()

android_caps.wd.find_element_by_id("message_ed_msgeditor").send_keys("recall message")
android_caps.wd.find_element_by_id("message_btn_sendtext").click()
msgtext = android_caps.wd.find_element_by_id("message_tv_msgtext")
action.long_press(el=msgtext).perform()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("撤回")').click()
try:
    android_caps.wd.find_element_by_id("button1").is_displayed()
    android_caps.wd.find_element_by_id("button1").click()
    try:
        android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("你撤回了一条消息")').is_displayed()
        print("消息撤回成功")
    except:
        print("消息撤回失败")
except:
    try:
        android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("你撤回了一条消息")').is_displayed()
        print("消息撤回成功")
    except:
        print("消息撤回失败")