# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
import login
log_in = True
while log_in:
    try:
        android_caps.wd.find_element_by_id("visitor_fast_register").is_displayed()  # 根据访客模式下的"快速注册"判断是否登录
        print ("正在执行登录流程....")
        login  # 调用登录模块
        sleep(5)
    except:
        print ("已登录")