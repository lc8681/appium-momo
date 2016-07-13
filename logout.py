# -*- coding: utf-8 -*-
# python学习，加油！

import android_caps
from time import sleep
sleep(5)
android_caps.wd.find_element_by_id("maintab_layout_profile").click()  # 点击个人帧
android_caps.wd.swipe(start_x=534, start_y=1534, end_x=534, end_y=415, duration=None)  # 向下滑动

sleep(3)
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("设置")').click()  # 按text查找

sleep(3)
android_caps.wd.find_element_by_id("setting_layout_logout").click()   # 点击"退出陌陌"

sleep(3)
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("退出当前帐号")').click()
android_caps.wd.find_element_by_id("button1").click()

sleep(3)
try:
    android_caps.wd.find_element_by_id("btn_ok").is_enabled()
    print("退出账号成功")

except:
    print("退出账号失败")

sleep(10)



