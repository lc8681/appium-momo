# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
from random import choice
import random
import sys
import find_toast
reload(sys)
sys.setdefaultencoding('utf-8')

sleep(5)
android_caps.self.find_element_by_id("maintab_layout_nearby").click()
android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("动态")').click()
sleep(5)  # 等待feed刷新完毕
# <====附近地点信息输出=====>
print "附近地点"+android_caps.self.find_element_by_id("site_name").text+\
      "("+android_caps.self.find_element_by_id("site_type_title").text+")"
print android_caps.self.find_element_by_id("site_desc").text
print "<====切换商圈操作====>"
android_caps.self.find_element_by_id("switch_site_button").click()
site_names = android_caps.self.find_elements_by_id("site_name")
name_list = []
for site_name in site_names:
    if site_name.get_attribute('resourceId') == 'com.immomo.momo:id/site_name':
        name_list.append(site_name)
choice_site = choice(name_list)
d_site_name = choice_site.text
choice_site.click()
pio_site = android_caps.self.find_element_by_id("site_name").text
android_caps.self.press_keycode(4)
if pio_site == d_site_name:
    print "切换商圈操作成功"
else:
    print "切换商圈操作失败!"

sleep(3)
print "当前商圈: "+android_caps.self.find_element_by_id("site_name").text+\
      "("+android_caps.self.find_element_by_id("site_type_title").text+")"
android_caps.self.swipe(start_x=527, start_y=1700, end_x=527, end_y=1480, duration=None)

#  <======判断是否有地点,如果有则向上滑动,再进行其他case
try:
    android_caps.self.find_element_by_id("layout_feed_map").is_displayed()
    feed_pio = android_caps.self.find_element_by_id("tv_feed_site").text
    print "发布了地理位置: "+android_caps.self.find_element_by_id("tv_feed_site").text
    android_caps.self.find_element_by_id("layout_feed_map").click()
    sleep(5)
    pio = android_caps.self.find_element_by_id("site_name").text
    if feed_pio == pio:      # 判断feed中的地点是否和地点feed中给出的地点一致
        print "地点动态加载正确"
        android_caps.self.press_keycode(4)
    else:
        print "feed没有出现在地点动态中!"
    android_caps.self.press_keycode(4)
    sleep(3)
except:
    print "没有发布地理位置"
print "距离: "+android_caps.self.find_element_by_id("layout_feed_distance").text
try:
    android_caps.self.find_element_by_id("tv_feed_comment").is_displayed()
    print android_caps.self.find_element_by_id("tv_feed_comment").text
except:
    print "没有评论数"
try:
    android_caps.self.find_element_by_id("tv_feed_read").is_displayed()
    print android_caps.self.find_element_by_id("tv_feed_read").text
except:
    print "没有阅读数"

# <=====判断点赞状态,用户没被点赞时\被点过赞\已经点过赞再取消赞=====>
try:
    zan_q = android_caps.self.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").'
                                                          'textMatches("(.*)赞")')
    a = int(zan_q.text[:-1])
    zan_q.is_displayed()
    android_caps.self.find_element_by_id("btn_feed_like").click()
    sleep(2)
    zan_h = android_caps.self.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").'
                                                           'textMatches("(.*)赞")')
    b = int(zan_h.text[:-1])
    if b >= a+1:
        print "点赞成功.(已经有赞了)"
    elif b <= a-1 or b == a or b == None:
        print "取消点赞成功."
    else:
        print "点赞失败"
except:
    android_caps.self.find_element_by_id("btn_feed_like").click()
    zan = android_caps.self.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").'
                                                           'textMatches("(.*)赞")')
    c = int(zan.text[:-1])
    if c >= 1:
        print "点赞成功"
    else:
        print "点赞失败"
sleep(3)
# <=====评论=====>
# android_caps.self.find_element_by_id("btn_feed_comment").click()
# android_caps.self.find_element_by_id("iv_feed_emote").click()
# android_caps.self.find_element_by_android_uiautomator\
#                 ('new UiSelector().resourceId("com.immomo.momo:id/imageview").index(2)').click()
# android_caps.self.find_element_by_android_uiautomator\
#                 ('new UiSelector().className("android.widget.LinearLayout").index(0)').click()
# if find_toast.find_toast("评论成功") == True:
#
# # <=====举报=====>
android_caps.self.find_element_by_id("btn_feed_more").click()
android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("举报")').click()
sleep(10)
if android_caps.self.find_element_by_id("web_title_textview").text == "动态举报":
    print "举报页面进入成功"
else:
    print "举报页面进入失败"
android_caps.self.find_element_by_accessibility_id("垃圾广告").click()
android_caps.self.find_element_by_accessibility_id("举报").click()
sleep(10)
try:
    android_caps.self.find_element_by_accessibility_id("举报已提交，我们将在2小时内进行处理（夜间时段会稍有延迟）").is_displayed()
    print "举报成功"
except:
    print "举报失败"
android_caps.self.press_keycode(4)
# <=====不感兴趣=====>
name = android_caps.self.find_element_by_id("tv_user_name").text          # 不感兴趣前
km = android_caps.self.find_element_by_id("layout_feed_distance").text
feed_time_q = android_caps.self.find_element_by_id("tv_feed_time").text

android_caps.self.find_element_by_id("btn_feed_more").click()
android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("不感兴趣")').click()
try:
    android_caps.self.find_element_by_id("ad_feed_btn_close").is_displayed()
    android_caps.self.find_element_by_id("ad_feed_btn_close").click()
    android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("不感兴趣")').click()
except:
    try:
        android_caps.self.find_element_by_id("lba_feed_btn_close").is_displayed()
        android_caps.self.find_element_by_id("lba_feed_btn_close").click()
        android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("不感兴趣")').click()
        name_h = android_caps.self.find_element_by_id("tv_user_name").text           # 不感兴趣后
        km_h = android_caps.self.find_element_by_id("layout_feed_distance").text
        feed_time_h = android_caps.self.find_element_by_id("tv_feed_time").text
        if name != name_h and km != km_h and feed_time_q != feed_time_h:
            print "不感兴趣操作成功."
        else:
            print "不感兴趣操作失败!"
    except:
        name_h = android_caps.self.find_element_by_id("tv_user_name").text           # 不感兴趣后
        km_h = android_caps.self.find_element_by_id("layout_feed_distance").text
        feed_time_h = android_caps.self.find_element_by_id("tv_feed_time").text
        if name != name_h and km != km_h and feed_time_q != feed_time_h:
            print "不感兴趣操作成功."
        else:
            print "不感兴趣操作失败!"
sleep(5)
# <=====附近人筛选=====>
android_caps.self.find_element_by_id("nearby_feed_filter").click()
print "<=====当前选择项=====>"
genderAll = android_caps.self.find_element_by_id("filter_radiobutton_genderAll")
genderMale = android_caps.self.find_element_by_id("filter_icon_radio_genderMale")
genderFemale = android_caps.self.find_element_by_id("filter_icon_radio_genderFemale")
ran_1 = [genderMale, genderFemale]
ran_2 = [genderAll, genderFemale]
ran_3 = [genderAll, genderMale]
if genderAll.get_attribute("checked") == "true":
    one = choice(ran_1)
    one.click()
    print "性别: "+one.text
elif genderMale.get_attribute("checked") == "true":
    two = choice(ran_2)
    two.click()
    print "性别: "+two.text
elif genderFemale.get_attribute("checked") == "true":
    three = choice(ran_3)
    three.click()
    print "性别: "+three.text
else:
    print "性别: 没有选中性别! "
if android_caps.self.find_element_by_id("tv_age_range").text == "全部":
    x_num = random.randint(160, 920)
    android_caps.self.swipe(start_x=969, start_y=960, end_x=x_num, end_y=960, duration=3000)
    sleep(1)
    android_caps.self.swipe(start_x=160, start_y=960, end_x=x_num, end_y=960, duration=3000)
set_age = android_caps.self.find_element_by_id("tv_age_range").text
print "年龄:"+set_age
android_caps.self.find_element_by_id("distance_filter_switch").click()
near = android_caps.self.find_element_by_id("distance_filter_switch").get_attribute("checked")
if near == "true":
    print "优先看距离近的?===>是"
else:
    print "优先看距离近的?===>否"
sleep(3)
android_caps.self.find_element_by_id("btn_ok").click()
sleep(5)
# <=====年龄是否符合筛选设置=====>
list_dis = []
for i in range(5):
    try:
        android_caps.self.find_element_by_id("ad_feed_btn_close").is_displayed()
        android_caps.self.find_element_by_id("ad_feed_btn_close").click()
        android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("不感兴趣")').click()
    except:
        try:
            android_caps.self.find_element_by_id("lba_feed_btn_close").is_displayed()
            android_caps.self.find_element_by_id("lba_feed_btn_close").click()
            android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("不感兴趣")').click()
        except:
            age = android_caps.self.find_element_by_id("badge_tv_age").text
            distance = android_caps.self.find_element_by_id("layout_feed_distance").text
            android_caps.self.swipe(start_x=508, start_y=1650, end_x=508, end_y=800, duration=None)

            try:
                android_caps.self.find_element_by_id("lba_feed_btn_close").is_displayed()
                android_caps.self.find_element_by_id("lba_feed_btn_close").click()
                android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("不感兴趣")').click()
            except:
                list_dis.append(float(distance[:-2]))       # 不要后两位的浮点类型

                if len(set_age) == 2:
                    try:
                        int(age) == int(set_age)
                    except:
                        print "年龄:"+age+"  错误(x)"+"设置的年龄为:"+set_age
                        sleep(10)
                        android_caps.self.quit()
                else:
                    if int(age) < int(set_age[1:2]) or int(age) > int(set_age[-3:-1]):
                        print "年龄:"+age+"  错误(x)"+"设置的年龄为:"+set_age
                        sleep(10)
                        android_caps.self.quit()
print "年龄都在范围内"
dis_a = sorted(list_dis)
print "扫描到的距离: "
print list_dis
print "优先显示距离近的排序: "
print dis_a
if near == "true":
    if list_dis == dis_a:
        print "优先显示距离近的排序正确"
        sleep(10)
        android_caps.self.quit()
    else:
        print "优先显示距离近的排序不正确!"
        sleep(10)
        android_caps.self.quit()

