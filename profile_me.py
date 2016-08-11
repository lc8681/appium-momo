# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
from random import choice
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sleep(5)
android_caps.wd.find_element_by_id("maintab_layout_profile").click()
print "昵称:"+android_caps.wd.find_element_by_id("myinfo_header_name").text
print "个性签名:"+android_caps.wd.find_element_by_id("myinfo_header_desc").text
android_caps.wd.find_element_by_id("myinfo_header_avatar").click()
# <=====输出个人profile页面信息=====>
try:
    android_caps.wd.find_element_by_accessibility_id("编辑").is_displayed()
    print("有编辑按钮")
except:
    print("没有编辑按钮!")
print "年龄:"+android_caps.wd.find_element_by_id("profile_tv_age").text+"岁"
print "星座:"+android_caps.wd.find_element_by_id("profile_tv_constellation").text

try:
    android_caps.wd.find_element_by_id("profile_tv_emotion").is_displayed()
    print "婚姻状态:"+android_caps.wd.find_element_by_id("profile_tv_emotion").text
except:
    print "没有找到婚姻状态"
print "距离&最后登录时间:"+android_caps.wd.find_element_by_id("profile_tv_distance_time").text
print "帐号等级:"+android_caps.wd.find_element_by_id("profile_account_grade_title").text
android_caps.wd.find_element_by_id("profile_account_grow_layout").click()
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("我的陌陌等级")').is_displayed()
    print "陌陌等级页面跳转正确"
except:
    print "陌陌等级页面跳转错误!"
android_caps.wd.press_keycode(4)
members = android_caps.wd.find_element_by_id("profile_account_vip_title").text
if members == "陌陌会员":
    print "会员等级:"+android_caps.wd.find_element_by_id("profile_account_vip_desc").text
elif members == "旗舰会员":
    print "会员等级:"+android_caps.wd.find_element_by_id("profile_account_vip_desc").text
else:
    print "会员等级:非会员"
android_caps.wd.find_element_by_id("profile_account_vip_layout").click()
if members == "陌陌会员":
    try:
        android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("会员中心")').is_displayed()
        print "会员中心跳转正确"
    except:
        print "会员中心跳转错误!"
elif members == "旗舰会员":
    try:
        android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("会员中心")').is_displayed()
        print "会员中心跳转正确"
    except:
        print "会员中心跳转错误!"
else:
    try:
        android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("确认支付")').is_displayed()
        print "购买会员跳转正确"
    except:
        print "购买会员跳转错误!"
android_caps.wd.press_keycode(4)
sleep(5)
android_caps.wd.swipe(start_x=513, start_y=1830, end_x=513, end_y=200, duration=None)
# android_caps.wd.swipe(start_x=513, start_y=1830, end_x=513, end_y=500, duration=None)  # 向下滑动

try:
    android_caps.wd.find_element_by_id("txt_join_group_count").is_displayed()
    print android_caps.wd.find_element_by_id("txt_join_group_count").text
    group = []
    group_names = android_caps.wd.find_elements_by_id("tv_groupname")
    decs = android_caps.wd.find_elements_by_id("tv_groupdec")
    for group_name in group_names:
        if group_name.get_attribute('resourceId') == 'com.immomo.momo:id/tv_groupname':
            group.append(group_name.text)
    for i in group:
        print i
except:
    print "没有找到群组信息"

try:
    android_caps.wd.find_element_by_id("tv_join_quanzi_count").is_displayed()
    print android_caps.wd.find_element_by_id("tv_join_quanzi_count").text
except:
    print "没有找到圈子信息"
android_caps.wd.find_element_by_id("tv_join_quanzi_count").click()
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("我的圈子")').is_displayed()
    print "我的圈子页面跳转正确"
except:
    print "我的圈子页面跳转错误!"
android_caps.wd.press_keycode(4)
sleep(5)
android_caps.wd.swipe(start_x=513, start_y=1830, end_x=513, end_y=1200, duration=None)

try:
    android_caps.wd.find_element_by_id("tv_like_movie_count").is_displayed()
    print android_caps.wd.find_element_by_id("tv_like_movie_count").text
except:
    print "没有找到电影信息"

try:
    android_caps.wd.find_element_by_id("tv_like_music_count").is_displayed()
    print android_caps.wd.find_element_by_id("tv_like_music_count").text
except:
    print "没有找到音乐信息"

try:
    android_caps.wd.find_element_by_id("tv_like_book_count").is_displayed()
    print android_caps.wd.find_element_by_id("tv_like_book_count").text
except:
    print "没有找到书籍信息"
android_caps.wd.swipe(start_x=513, start_y=1830, end_x=513, end_y=1200, duration=None)
sleep(2)
try:
    android_caps.wd.find_element_by_id("tv_focus_live_count").is_displayed()
    print android_caps.wd.find_element_by_id("tv_focus_live_count").text
except:
    print "没有找到关注的艺人信息"
android_caps.wd.find_element_by_id("profile_layout_focus_live").click()
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("TA关注的播主")').is_displayed()
    print "关注的主播页面跳转正确"
except:
    print "关注的主播页面跳转错误"
android_caps.wd.press_keycode(4)
try:
    android_caps.wd.find_element_by_id("profile_tv_gift").is_displayed()
    print android_caps.wd.find_element_by_id("profile_tv_gift").text
except:
    print "没有找到收到的礼物信息"

try:
    android_caps.wd.find_element_by_id("profile_txt_gifttitle").is_displayed()
    print android_caps.wd.find_element_by_id("profile_txt_gifttitle").text
except:
    print "没有找到我喜欢的礼物信息"
android_caps.wd.find_element_by_id("profile_layout_gift").click()
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("我喜欢的礼物清单")').is_displayed()
    print "我喜欢的礼物页面跳转正确"
except:
    print "我喜欢的礼物页面跳转错误"
android_caps.wd.press_keycode(4)
android_caps.wd.quit()