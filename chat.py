# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
from random import choice
import random
sleep(5)
android_caps.wd.find_element_by_id("maintab_layout_chat").click()
try:
    android_caps.wd.find_element_by_id("chatlist_item_tv_name").is_displayed()
    android_caps.wd.find_element_by_id("chatlist_item_iv_face").is_displayed()
    print "消息cell加载成功"
except:
    print "消息cell加载失败!"

# <=====忽略未读=====>
android_caps.wd.find_element_by_id("action_clear_unread").click()
android_caps.wd.find_element_by_id("button1").click()
try:
    android_caps.wd.find_element_by_id("chatlist_item_tv_status_new").is_displayed()
    android_caps.wd.find_element_by_id("tab_item_tv_badge").is_displayed()
    print "聊天气泡未被清除!"
except:
    print "清除聊天气泡正常."

# <=====搜索框=====>
android_caps.wd.find_element_by_android_uiautomator\
                ('new UiSelector().className("android.widget.TextView").text("搜索")').click()
# ----搜索陌陌号----
android_caps.wd.find_element_by_id("toolbar_search_edittext").send_keys("10000")
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("陌陌号:10000")').is_displayed()
    print "搜索陌陌号功能正常."
except:
    print "搜索陌陌号功能异常."
# ----搜索附近群组----
def search_clear(text):
    android_caps.wd.keyevent(123)
    for i in range(0, len(text)):
        android_caps.wd.keyevent(67)
adr = android_caps.wd.find_element_by_id("toolbar_search_edittext")
adr.click()
context2 = adr.get_attribute('text')
search_clear(context2)
android_caps.wd.find_element_by_id("fullsearch_btn_nearbygroup").click()
try:
    android_caps.wd.find_element_by_id("tv_name").is_displayed()
    print "热门关键字标签显示成功"
except:
    print "热门关键字标签显示异常!"
android_caps.wd.find_element_by_id("tv_name").click()
try:
    android_caps.wd.find_element_by_id("group_item_join_group").is_displayed()
    android_caps.wd.find_element_by_id("group_item_tv_name").is_displayed()
    print "热门群组加载成功"
except:
    print "热门群组加载异常!"
android_caps.wd.press_keycode(4)
android_caps.wd.find_element_by_id("toolbar_search_edittext").send_keys("28540755")
android_caps.wd.press_keycode(66)
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("陌陌新奇馆")').is_displayed()
    android_caps.wd.find_element_by_id("group_item_join_group").is_displayed()
    print "搜索群号正常."
except:
    print "搜索群号异常."
android_caps.wd.press_keycode(4)
sleep(2)
android_caps.wd.press_keycode(4)
sleep(2)
android_caps.wd.press_keycode(4)
sleep(2)
android_caps.wd.quit()
