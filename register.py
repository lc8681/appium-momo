# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
from random import choice
import random
sleep(5)
android_caps.wd.find_element_by_id("maintab_layout_profile").click()   # 点击个人帧
sleep(1)
android_caps.wd.find_element_by_id("visitor_btn_reg").click()    # 点击注册按钮
sleep(5)
# <<<-------输入昵称------->>>
android_caps.wd.find_element_by_id("rg_et_name").send_keys("The robot")
android_caps.wd.find_element_by_id("btn_next").click()
# <<<-------添加头像------->>>
android_caps.wd.find_element_by_id("rg_iv_userphoto").click()
try:
    android_caps.wd.find_element_by_id("tip_layout").is_displayed()
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("上传真实头像，认识新朋友速度提升67%")')
    print("蓝条显示正常;文案显示正确")
except:
    print("未展示蓝条")
android_caps.wd.find_element_by_id("tip_layout").click()
try:
    android_caps.wd.find_element_by_id("tip_layout").is_displayed()
    print("点击蓝条没有消失")
    quit()
except:
    print("点击蓝条消失")
android_caps.wd.tap([(405, 376), (405, 376)], None)
android_caps.wd.find_element_by_id("imagefactory_btn2").click()
# <<<-------选择生日------->>>
android_caps.wd.find_element_by_id("rg_tv_birthday").click()
android_caps.wd.find_element_by_id("date_picker_year").click()
android_caps.wd.swipe(start_x=549, start_y=1190, end_x=549, end_y=1692, duration=3000)
sleep(3)
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("1986")').click()
android_caps.wd.find_element_by_id("button1").click()
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("选择生日")').is_displayed()
    print("生日添加失败!")
    quit()
except:
    print("添加生日成功.")
# <<<-------选择家乡------->>>
android_caps.wd.find_element_by_id("rg_tv_hometown").click()
sleep(3)
android_caps.wd.swipe(start_x=324, start_y=1039, end_x=324, end_y=637, duration=3000)
sleep(3)
android_caps.wd.find_element_by_id("button1").click()
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("选择家乡")').is_displayed()
    print("家乡添加失败!")
    quit()
except:
    print("家乡添加成功.")
# <<<-------选择性别(随机选择)------->>>
male = android_caps.wd.find_element_by_id("rg_radiobutton_male")
female = android_caps.wd.find_element_by_id("rg_radiobutton_female")
gender = [male, female]
if choice(gender) == male:
    male.click()
    print("性别: 男")
else:
    choice(gender) == female
    female.click()
    print("性别: 女")
# <<<----------------------------->>>
android_caps.wd.find_element_by_id("btn_next").click()
try:
    android_caps.wd.find_element_by_id("button1").is_displayed()
    android_caps.wd.find_element_by_id("button1").click()
except:
    sleep(1)
# front_phone = "160 2888 9"
# space = sleep(1)
phone = '160 '+'2888 '+'9'+"".join(random.choice("123") for i in range(3))
# phone = "16028889456"
reg = True
while reg:
    try:
        android_caps.wd.find_element_by_android_uiautomator('new UiSelector().textContains("160 ")').is_displayed()
        print("正在重新尝试手机号")
        def username_clear(text):
            android_caps.wd.keyevent(123)
            for i in range(0, len(text)):
                android_caps.wd.keyevent(67)
        adr = android_caps.wd.find_element_by_id("rg_et_phone")
        adr.click()
        context2 = adr.get_attribute('text')
        username_clear(context2)
        sleep(3)
        android_caps.wd.find_element_by_id("rg_et_phone").send_keys(phone)
        sleep(5)
        android_caps.wd.press_keycode(4)
        android_caps.wd.find_element_by_id("btn_next").click()
        android_caps.wd.find_element_by_id("button1").click()
        code1 = android_caps.wd.find_element_by_android_uiautomator\
                ('new UiSelector().className("android.widget.EditText").index(2)')
        sleep(2)
        code1.send_keys("1 6 0 2 0 0")
        android_caps.wd.find_element_by_id("rg_et_resend").click()
        try:
            android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("不是我的，完成注册")').is_displayed()
            android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("不是我的，完成注册")').click()
            print"注册成功,手机号:"+phone
            reg = False
            sleep(10)
            android_caps.wd.quit()
        except:
            try:
                android_caps.wd.find_element_by_id("nearby_match_like").is_displayed()
                print"手机号已注册,手机号:"+phone
                reg = False
                sleep(10)
                android_caps.wd.quit()
            except:
                print("手机号已经注册,请重新再试.")
                android_caps.wd.find_element_by_id("button2").click()
                android_caps.wd.press_keycode(4)
                android_caps.wd.find_element_by_id("button2").click()
                reg = True
    except:
        android_caps.wd.find_element_by_id("rg_et_phone").send_keys(phone)
        android_caps.wd.find_element_by_id("rg_et_password").send_keys("momo1234")
        android_caps.wd.find_element_by_id("btn_next").click()
        android_caps.wd.find_element_by_id("button1").click()
        code1 = android_caps.wd.find_element_by_android_uiautomator\
                ('new UiSelector().className("android.widget.EditText").index(2)')
        sleep(2)
        code1.send_keys("1 6 0 2 0 0")
        android_caps.wd.find_element_by_id("rg_et_resend").click()
        try:
            android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("不是我的，完成注册")').is_displayed()
            android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("不是我的，完成注册")').click()
            print"注册成功,手机号:"+phone
            reg = False
            sleep(10)
            android_caps.wd.quit()
        except:
            print("手机号已经注册,请重新再试.")
            android_caps.wd.find_element_by_id("button2").click()
            android_caps.wd.press_keycode(4)
            android_caps.wd.find_element_by_id("button2").click()










