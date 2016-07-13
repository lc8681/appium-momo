# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
# <-------以下判断是否登录,如果登录直接发布动态;如果未登录调用login.py进行登录操作后再走发布动态流程------->

log_in = True
while log_in:
    try:
        android_caps.wd.find_element_by_id("visitor_fast_register").is_displayed()
        print ("正在执行登录流程....")
        import login
    except:
        print ("已登录")
# <--------------- 以 下 为 登 录 后 ---------------->
        android_caps.wd.swipe(start_x=190, start_y=1550, end_x=1000, end_y=1550, duration=None)  # 往左滑动进入动态
        android_caps.wd.find_element_by_id("feedlist_menu_publish").click()  # 点击发布动态按钮
        android_caps.wd.find_element_by_id("signeditor_tv_text").send_keys("test")
        android_caps.wd.find_element_by_id("layout_add_more").click()
        android_caps.wd.find_element_by_id("layout_add_emotion").click()
        android_caps.wd.swipe(start_x=157, start_y=1240, end_x=157, end_y=1240, duration=None)
        log_in = False


print ("流程继续ing....")





