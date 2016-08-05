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
android_caps.wd.find_element_by_id("maintab_layout_nearby").click()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("动态")').click()
sleep(5)  # 等待feed刷新完毕
'''
# <====附近地点信息输出=====>
print "附近地点"+android_caps.wd.find_element_by_id("site_name").text+\
      "("+android_caps.wd.find_element_by_id("site_type_title").text+")"
print android_caps.wd.find_element_by_id("site_desc").text
android_caps.wd.swipe(start_x=527, start_y=1700, end_x=527, end_y=1480, duration=None)
feed_time = android_caps.wd.find_element_by_id("tv_feed_time").text
#  <======判断是否有地点,如果有则向上滑动,再进行其他case
try:
    android_caps.wd.find_element_by_id("layout_feed_map").is_displayed()
    print "发布了地理位置: "+android_caps.wd.find_element_by_id("tv_feed_site").text
    android_caps.wd.find_element_by_id("layout_feed_map").click()
    sleep(5)
    pio_time = android_caps.wd.find_element_by_id("tv_feed_time").text
    if feed_time == pio_time:      # 判断feed中的首位用户是否和地点feed中的首位用户一致
        print "地点动态加载正确"
        android_caps.wd.press_keycode(4)
    else:
        print "feed没有出现在地点动态中!"
    android_caps.wd.press_keycode(4)
    sleep(3)
except:
    print "没有发布地理位置"
print "距离: "+android_caps.wd.find_element_by_id("layout_feed_distance").text
try:
    android_caps.wd.find_element_by_id("tv_feed_comment").is_displayed()
    print android_caps.wd.find_element_by_id("tv_feed_comment").text
except:
    print "没有评论数"
try:
    android_caps.wd.find_element_by_id("tv_feed_read").is_displayed()
    print android_caps.wd.find_element_by_id("tv_feed_read").text
except:
    print "没有阅读数"

# <=====判断点赞状态,用户没被点赞时\被点过赞\已经点过赞再取消赞=====>
try:
    zan_q = android_caps.wd.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").'
                                                          'textMatches("(.*)赞")')
    a = int(zan_q.text[:-1])
    zan_q.is_displayed()
    android_caps.wd.find_element_by_id("btn_feed_like").click()
    sleep(2)
    zan_h = android_caps.wd.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").'
                                                           'textMatches("(.*)赞")')
    b = int(zan_h.text[:-1])
    if b >= a+1:
        print "点赞成功.(已经有赞了)"
    elif b <= a-1 or b == a or b == None:
        print "取消点赞成功."
    else:
        print "点赞失败"
except:
    android_caps.wd.find_element_by_id("btn_feed_like").click()
    zan = android_caps.wd.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").'
                                                           'textMatches("(.*)赞")')
    c = int(zan.text[:-1])
    if c >= 1:
        print "点赞成功"
    else:
        print "点赞失败"

sleep(3)
'''
# <=====举报=====>
android_caps.wd.find_element_by_id("btn_feed_more").click()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("举报")').click()
sleep(10)
if android_caps.wd.find_element_by_id("web_title_textview").text == "动态举报":
    print "举报页面进入成功"
else:
    print "举报页面进入失败"
android_caps.wd.find_element_by_accessibility_id("垃圾广告").click()
android_caps.wd.find_element_by_accessibility_id("举报").click()
sleep(10)
try:
    android_caps.wd.find_element_by_accessibility_id("举报已提交，我们将在2小时内进行处理（夜间时段会稍有延迟）").is_displayed()
    print "举报成功"
except:
    print "举报失败"
android_caps.wd.press_keycode(4)
# <=====不感兴趣=====>
name = android_caps.wd.find_element_by_id("tv_user_name").text          # 不感兴趣前
km = android_caps.wd.find_element_by_id("layout_feed_distance").text
feed_time_q = android_caps.wd.find_element_by_id("tv_feed_time").text
age_q = android_caps.wd.find_element_by_id("badge_tv_age").text

android_caps.wd.find_element_by_id("btn_feed_more").click()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("不感兴趣")').click()

name_h = android_caps.wd.find_element_by_id("tv_user_name").text           # 不感兴趣后
km_h = android_caps.wd.find_element_by_id("layout_feed_distance").text
feed_time_h = android_caps.wd.find_element_by_id("tv_feed_time").text
age_h = android_caps.wd.find_element_by_id("badge_tv_age").text

if name != name_h and km != km_h and feed_time_q != feed_time_h and age_q != age_h:
    print "不感兴趣操作成功."
else:
    print "不感兴趣操作失败!"
android_caps.wd.quit()

