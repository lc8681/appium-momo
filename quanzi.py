# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from random import choice
import random
sleep(5)
android_caps.wd.find_element_by_id("maintab_layout_profile").click()
android_caps.wd.find_element_by_id("quanzi_layout").click()
sleep(5)
'''
try:
    android_caps.wd.find_element_by_accessibility_id("进入圈子").is_displayed()
    print("显示圈子升级弹窗.")
    android_caps.wd.find_element_by_accessibility_id("进入圈子").click()
except:
    print("没有显示圈子升级弹窗.")
'''
android_caps.wd.find_element_by_class_name("android.widget.EditText").click()
android_caps.wd.find_element_by_class_name("android.widget.EditText").send_keys("mmqa")
try:
    android_caps.wd.find_element_by_accessibility_id("已加入").is_displayed()
    print("已经加入此圈子")
    android_caps.wd.find_element_by_accessibility_id("已加入").click()
except:
    print("没有加入此圈子,自动加入.")
    android_caps.wd.find_element_by_accessibility_id("加入").click()
    android_caps.wd.find_element_by_accessibility_id("已加入").click()

# <=====发布帖子流程=====>
android_caps.wd.find_element_by_accessibility_id(" 发布帖子").click()
sleep(3)
android_caps.wd.find_element_by_id("tv_topic").send_keys("quanzi_test")
android_caps.wd.find_element_by_id("signeditor_tv_text").send_keys("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
android_caps.wd.find_element_by_id("layout_add_pic").click()
android_caps.wd.tap([(398, 1421), (398, 421)], None)
sleep(1)
android_caps.wd.find_element_by_id("imagepager_check").click()
android_caps.wd.find_element_by_id("imagepager_send").click()
# ----删除图片---
android_caps.wd.find_element_by_id("bean_item_remove_iv").click()
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("视频")').is_displayed()
    print("删除图片成功")
except:
    print("删除图片失败!")
android_caps.wd.find_element_by_id("layout_add_pic").click()
android_caps.wd.tap([(398, 1421), (398, 421)], None)
sleep(1)
android_caps.wd.find_element_by_id("imagepager_check").click()
android_caps.wd.find_element_by_id("imagepager_send").click()
android_caps.wd.find_element_by_id("layout_site").click()
sleep(5)
android_caps.wd.find_element_by_android_uiautomator\
                ('new UiSelector().className("android.widget.LinearLayout").index(2)').click()
sleep(5)
poi = android_caps.wd.find_element_by_id("tv_feed_site_selected")

try:
    poi.is_displayed()
    print "地点选择:"+poi.text
except:
    print "没有获取到地点"
    sleep(20)
    android_caps.wd.quit()
android_caps.wd.find_element_by_accessibility_id("发布").click()
sleep(10)
try:
    android_caps.wd.find_element_by_accessibility_id("1分钟前").is_displayed()
    print("发布成功.")
except:
    print("发布失败!")
# <======操作帖子======>
android_caps.wd.find_element_by_accessibility_id("1分钟前").click()
try:
    android_caps.wd.find_element_by_accessibility_id("帖子置顶","帖子加精","隐藏帖子","禁言并删帖","举报并删帖").is_displayed()
    print("身份:管理员.")
except:
    print("身份:非管理员.")
android_caps.wd.find_element_by_accessibility_id("帖子加精").click()
android_caps.wd.find_element_by_android_uiautomator\
                ('new UiSelector().className("android.widget.Button").index(1)').click()
sleep(10)
android_caps.wd.quit()