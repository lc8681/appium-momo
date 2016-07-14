# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep

android_caps.wd.find_element_by_id("maintab_layout_profile").click()   # 点击个人帧
sleep(1)
android_caps.wd.find_element_by_id("visitor_btn_login").click()    # 点击登录按钮

# <-------------判断用户名或密码是否正确,如果不正确重新输入;如果正确直接登录---------------->
login_again = True
while login_again:
    try:
        android_caps.wd.find_element_by_id("login_et_momoid").is_displayed()
        def username_clear(text):
            android_caps.wd.keyevent(123)
            for i in range(0, len(text)):
                android_caps.wd.keyevent(67)
        adr = android_caps.wd.find_element_by_id("login_et_momoid")
        adr.click()
        context2 = adr.get_attribute('text')
        username_clear(context2)

        username = raw_input("请输入用户名:")
        android_caps.wd.find_element_by_id("login_et_momoid").send_keys(username)  # 输入用户名
        android_caps.wd.find_element_by_id("login_et_pwd").click()
        sleep(1)
        android_caps.wd.press_keycode(67)    # 删除键
        android_caps.wd.press_keycode(67)
        android_caps.wd.press_keycode(67)
        android_caps.wd.press_keycode(67)
        android_caps.wd.press_keycode(67)
        android_caps.wd.press_keycode(67)
        android_caps.wd.press_keycode(67)
        android_caps.wd.press_keycode(67)
        android_caps.wd.press_keycode(67)
        android_caps.wd.press_keycode(67)
        android_caps.wd.press_keycode(67)
        android_caps.wd.press_keycode(67)
        android_caps.wd.press_keycode(67)

        password = raw_input("请输入密码:")
        android_caps.wd.find_element_by_id("login_et_pwd").send_keys(password)     # 输入密码
        android_caps.wd.find_element_by_id("btn_ok").click()   # 确定登录
        sleep(5)
        try:
            android_caps.wd.find_element_by_id("nearby_match_like").is_displayed()
            login_again = False
        except:
            print ("用户名或密码错误,正在重启登录流程....")
            android_caps.wd.find_element_by_id("button2").click()

    except:
        print ("用户名或密码错误,正在重启登录流程....")
        android_caps.wd.find_element_by_id("button2").click()

print("登录成功")

