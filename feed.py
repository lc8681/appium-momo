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
sleep(5)

zan_q = android_caps.wd.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").'
                                                          'textMatches("(.*)赞")').text
a = int(zan_q[:-1])
android_caps.wd.find_element_by_id("btn_feed_like").click()
sleep(2)
zan_h = android_caps.wd.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").'
                                                          'textMatches("(.*)赞")').text
b = int(zan_h[:-1])
print a
print b
if a > b:
    print "12345"
elif b == a+1:
    print "点赞成功"
else:
    print "点赞失败!"
'''
1. 判断有无赞,如没有,直接点赞按钮,判断赞数是否+1
2. 如果有赞,走上面逻辑
    '''