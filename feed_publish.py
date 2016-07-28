# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
from random import choice
import login
# <-------以下判断是否登录,如果登录直接发布动态;如果未登录调用login.py进行登录操作后再走发布动态流程------->
log_in = True
while log_in:
    try:
        android_caps.wd.find_element_by_id("visitor_fast_register").is_displayed()  # 根据访客模式下的"快速注册"判断是否登录
        print ("正在执行登录流程....")
        login  # 调用登录模块
        sleep(5)
    except:
        print ("已登录")
        android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("动态")').click()  # 点击动态tab
        android_caps.wd.find_element_by_id("feedlist_menu_publish").click()  # 点击发布动态按钮
        check_text = raw_input("请输入动态内容:")
        android_caps.wd.find_element_by_id("signeditor_tv_text").send_keys(check_text)  # 输入测试文本test

        pic = android_caps.wd.find_element_by_id("layout_add_pic")
        video = android_caps.wd.find_element_by_id("layout_add_video")
        more = android_caps.wd.find_element_by_id("layout_add_more")
        ran = [pic, video, more]
        if choice(ran) == video:
            video.click()
            android_caps.wd.find_element_by_id("recorder_change_camera").click()
            sleep(3)
            android_caps.wd.find_element_by_id("record_button").click()
            sleep(40)
            android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("完成")').click()
            sleep(20)
            log_in = False
        elif choice(ran) == pic:
            pic.click()
            android_caps.wd.tap([(398, 1421), (398, 421)], None)
            sleep(1)
            android_caps.wd.find_element_by_id("imagepager_check").click()
            android_caps.wd.find_element_by_id("imagepager_send").click()
            sleep(2)
            log_in = False
        else:
            more.click()
            sleep(1)
            android_caps.wd.find_element_by_id("layout_add_emotion").click()
            sleep(1)
            android_caps.wd.tap([(395, 1264), (395, 1264)], None)
            log_in = False
else:
    try:
        android_caps.wd.find_element_by_id("tv_feed_site_selected").is_displayed()
        print("地点显示正常!!")
    except:
            print("没有拿到地点!!")
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("发布")').click()
sleep(10)
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("1分钟前")')
    print "发布成功,发布动态流程结束"
    sleep(20)
    android_caps.wd.quit()
except:
    print "发布失败"
    sleep(20)
    android_caps.wd.quit()





