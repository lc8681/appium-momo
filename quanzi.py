# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from random import choice
import random
# print "<-------------登录流程begin---------------->"
# sleep(5)
# try:  # 判断是否处于登录状态,如果登录则直接进入圈子,如果未登录执行登录流程
#     android_caps.wd.find_element_by_id("visitor_fast_register").is_displayed()
#     print "$ 帐号未登录,执行登录流程..."
#     android_caps.wd.find_element_by_id("maintab_layout_profile").click()   # 点击个人帧
#     sleep(2)
#     android_caps.wd.find_element_by_id("visitor_btn_login").click()    # 点击登录按钮
#     sleep(2)
#     def username_clear(text):
#         android_caps.wd.keyevent(123)
#         for i in range(0, len(text)):
#             android_caps.wd.keyevent(67)
#     adr = android_caps.wd.find_element_by_id("login_et_momoid")
#     adr.click()
#     context2 = adr.get_attribute('text')
#     username_clear(context2)
#
#     android_caps.wd.find_element_by_id("login_et_momoid").send_keys("219530396")  # 输入用户名
#     android_caps.wd.find_element_by_id("login_et_pwd").click()
#     sleep(1)
#     android_caps.wd.find_element_by_id("login_et_pwd").send_keys("momo1234")     # 输入密码
#     android_caps.wd.find_element_by_id("btn_ok").click()   # 确定登录
#     sleep(10)
#     try:
#         android_caps.wd.find_element_by_id("maintab_layout_nearby").is_displayed()
#         print "$ 帐号登录成功..."
#     except:
#         print "$ 账号登录失败"
#
# except:
#     print "帐号已登录,执行圈子流程..."

print "<-------------登录流程end,进入圈子begin---------------->"
android_caps.wd.find_element_by_id("maintab_layout_profile").click()   # 点击个人帧
android_caps.wd.find_element_by_id("quanzi_layout").click()   # 点击圈子入口
sleep(30)
print "<-------------进入圈子end,创建圈子begin---------------->"
android_caps.wd.find_element_by_id("group_btn_layout").click()
sleep(30)
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().className("android.view.View").index(3)').click()
android_caps.wd.find_element_by_class_name("android.widget.EditText").send_keys("AutoQA")
sleep(3)
android_caps.wd.find_element_by_accessibility_id("下一步").click()
sleep(3)
android_caps.wd.find_element_by_accessibility_id("添加头像").click()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("本地相册")').click()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector()'
                                                    '.className("android.widget.RelativeLayout").index(1)').click()
sleep(3)
android_caps.wd.find_element_by_id("imagefactory_btn2").click()
sleep(3)
android_caps.wd.find_element_by_id("imagefactory_btn2").click()
sleep(3)
android_caps.wd.find_element_by_accessibility_id("选择圈子分类 ").click()
android_caps.wd.find_element_by_accessibility_id("情感交流 ").click()
sleep(1)
android_caps.wd.find_element_by_accessibility_id("下一步").click()
android_caps.wd.find_element_by_class_name("android.widget.EditText").send_keys("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
android_caps.wd.find_element_by_accessibility_id("完成").click()
sleep(15)
try:
    android_caps.wd.find_element_by_accessibility_id("圈子创建成功").is_displayed()
    print "$ 圈子创建成功!"
    android_caps.wd.find_element_by_accessibility_id("进入圈子").click()
except:
    print "$ 圈子创建失败!!!"

print "<-------------创建圈子end,发布帖子begin---------------->"
sleep(15)
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().className("android.view.View").index(17)').click()
sleep(3)
android_caps.wd.find_element_by_id("tv_topic").send_keys("quanzi_test")
android_caps.wd.find_element_by_id("signeditor_tv_text").send_keys("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
pic = android_caps.wd.find_element_by_id("layout_add_pic")
video = android_caps.wd.find_element_by_id("layout_add_video")
ran = [pic, video]
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
    android_caps.wd.find_element_by_id("checkbox").click()
    # android_caps.wd.tap([(398, 1421), (398, 421)], None)
    sleep(1)
    android_caps.wd.find_element_by_id("multpic_main_send").click()
    sleep(2)
    log_in = False

android_caps.wd.find_element_by_id("layout_site").click()
sleep(5)
android_caps.wd.find_element_by_id("site_name").click()
try:
    android_caps.wd.find_element_by_id("tv_feed_site_selected").is_displayed()
    print "$ 发布界面地点显示正常"
except:
    print "$ 发布界面地点显示不正常"
android_caps.wd.find_element_by_accessibility_id("发布").click()
sleep(5)
try:  # 用"刚刚"来判断是否发布成功
    android_caps.wd.find_element_by_accessibility_id("刚刚").is_displayed()
    print "$ 发布成功"
except:
    try:  # 用"1分钟前"来判断是否发布成功
        android_caps.wd.find_element_by_accessibility_id("1分钟前").is_displayed()
        print "$ 发布成功"
    except:
        print "$ 发布失败"
    print "$ 发布失败"

print "<-------------发布帖子end,评论begin---------------->"
