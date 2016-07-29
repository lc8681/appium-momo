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
print "婚姻状态:"+android_caps.wd.find_element_by_id("profile_tv_emotion").text
print "距离&最后登录时间:"+android_caps.wd.find_element_by_id("profile_tv_distance_time").text
print android_caps.wd.find_element_by_id("txt_join_feed_count").text
print "帐号等级:"+android_caps.wd.find_element_by_id("profile_account_grade_title").text
members = android_caps.wd.find_element_by_id("profile_account_vip_title").text
if members == "陌陌会员":
    print "会员等级:"+android_caps.wd.find_element_by_id("profile_account_vip_desc").text
elif members == "旗舰会员":
    print "会员等级:"+android_caps.wd.find_element_by_id("profile_account_vip_desc").text
else:
    print "会员等级:非会员"
android_caps.wd.swipe(start_x=513, start_y=1830, end_x=513, end_y=800, duration=None)  # 向下滑动
