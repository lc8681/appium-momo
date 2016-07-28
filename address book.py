# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
from random import choice
import random

android_caps.wd.find_element_by_id("maintab_layout_contact").click()
sleep(5)
# <========获取"好友\关注\粉丝"数量========>
# 好友
friends = android_caps.wd.find_element_by_android_uiautomator('new UiSelector().textMatches("好友(.*)")').text
print "<---"+friends+"--->"
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_name").is_displayed()
    print("昵称正确.")
except:
    print("昵称异常!")
try:
    android_caps.wd.find_element_by_id("badge_tv_age").is_displayed()
    print("年龄icon正确.")
except:
    print("年龄icon异常!")
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_distance").is_displayed()
    print("距离显示正确.")
except:
    print("距离显示异常!")
try:
    android_caps.wd.find_element_by_id("userlist_tv_time").is_displayed()
    print("最后在线时间正确.")
except:
    print("最后在线时间异常!")
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_sign").is_displayed()
    print("签名显示正确.")
except:
    print("签名显示异常!")
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_special").is_displayed()
    print("特别好友icon正确.")
except:
    print("特别好友icon异常!")
# 关注
android_caps.wd.find_element_by_android_uiautomator\
                ('new UiSelector().className("android.support.v7.app.g").index(0)').click()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
sleep(5)
focus = android_caps.wd.find_element_by_android_uiautomator('new UiSelector().textMatches("关注(.*)")').text
print "<---"+focus+"--->"
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_name").is_displayed()
    print("昵称正确.")
except:
    print("昵称异常!")
try:
    android_caps.wd.find_element_by_id("badge_tv_age").is_displayed()
    print("年龄icon正确.")
except:
    print("年龄icon异常!")
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_distance").is_displayed()
    print("距离显示正确.")
except:
    print("距离显示异常!")
try:
    android_caps.wd.find_element_by_id("userlist_tv_time").is_displayed()
    print("最后在线时间正确.")
except:
    print("最后在线时间异常!")
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_sign").is_displayed()
    print("签名显示正确.")
except:
    print("签名显示异常!")

# 粉丝
android_caps.wd.find_element_by_android_uiautomator\
                ('new UiSelector().className("android.support.v7.app.g").index(0)').click()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("粉丝")').click()
sleep(5)
fans = android_caps.wd.find_element_by_android_uiautomator('new UiSelector().textMatches("粉丝(.*)")').text
print "<---"+fans+"--->"
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_name").is_displayed()
    print("昵称正确.")
except:
    print("昵称异常!")
try:
    android_caps.wd.find_element_by_id("badge_tv_age").is_displayed()
    print("年龄icon正确.")
except:
    print("年龄icon异常!")
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_distance").is_displayed()
    print("距离显示正确.")
except:
    print("距离显示异常!")
try:
    android_caps.wd.find_element_by_id("userlist_tv_time").is_displayed()
    print("最后在线时间正确.")
except:
    print("最后在线时间异常!")
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_sign").is_displayed()
    print("签名显示正确.")
except:
    print("签名显示异常!")

# <========获取群组数量========>
android_caps.wd.find_element_by_android_uiautomator\
                ('new UiSelector().className("android.support.v7.app.g").index(1)').click()
sleep(5)
group = android_caps.wd.find_element_by_android_uiautomator('new UiSelector().textMatches("群组(.*)")').text
print "<---"+group+"--->"
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_name").is_displayed()
    print("群组名称正确.")
except:
    print("群组名称异常!")
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_sign").is_displayed()
    print("群组签名正确.")
except:
    print("群组签名异常!")
# <========获取认证账号数量========>
android_caps.wd.find_element_by_android_uiautomator\
                ('new UiSelector().className("android.support.v7.app.g").index(2)').click()
sleep(5)
certification = android_caps.wd.find_element_by_android_uiautomator('new UiSelector().textMatches("认证帐号(.*)")').text
print "<---"+certification+"--->"
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_name").is_displayed()
    print("认证帐号名称正确.")
except:
    print("认证帐号名称异常!")
try:
    android_caps.wd.find_element_by_id("userlist_item_tv_sign").is_displayed()
    print("认证帐号签名正确.")
except:
    print("认证帐号签名异常!")
android_caps.wd.quit()