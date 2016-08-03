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
feed_name = android_caps.wd.find_element_by_id("tv_user_name").text
#  <======判断是否有地点,如果有向上滑动200,再进行其他case
try:
    print("附近动态中的用户名: ")+feed_name
    android_caps.wd.find_element_by_id("layout_feed_map").is_displayed()
    print("有地理位置")
    android_caps.wd.find_element_by_id("layout_feed_map").click()
    sleep(3)
    pio_name = android_caps.wd.find_element_by_id("tv_user_name").text
    print("地点动态中的用户名: ")+pio_name
    android_caps.wd.press_keycode(4)
    # android_caps.wd.swipe(start_x=513, start_y=1830, end_x=513, end_y=1430, duration=None)
except:
    print "没有地理位置"

try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").'
                                                          'textMatches("(.*)赞")').is_displayed()
    zan_q = android_caps.wd.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").'
                                                          'textMatches("(.*)赞")').text
    a = int(zan_q[:-1])
    android_caps.wd.find_element_by_id("btn_feed_like").click()
    sleep(2)
    zan_h = android_caps.wd.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").'
                                                              'textMatches("(.*)赞")').text
    b = int(zan_h[:-1])
    if a > b:
        print "取消点赞成功"
    elif b == a+1:
        print "点赞成功"
    else:
        print "点赞失败!"

except:
    android_caps.wd.find_element_by_id("btn_feed_like").click()
    try:
        android_caps.wd.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").'
                                                              'textMatches("1赞")').is_displayed()
        print "点赞成功"
    except:
        print "点赞失败!"
sleep(10)
android_caps.wd.quit()
'''
1. 判断有无赞,如没有,直接点赞按钮,判断赞数是否+1
2. 如果有赞,走上面逻辑
    '''