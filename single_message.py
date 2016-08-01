# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
from random import choice
from appium.webdriver.common.touch_action import TouchAction


action = TouchAction(android_caps.wd)
android_caps.wd.find_element_by_id("maintab_layout_contact").click()
android_caps.wd.find_element_by_id("friend_action_search").click()
android_caps.wd.find_element_by_id("toolbar_search_edittext").send_keys("220850234")
try:
    android_caps.wd.find_element_by_id("section_title").click()
except:
    print("没有搜素到用户")
android_caps.wd.find_element_by_id("profile_layout_start_chat").click()

# <---------文本消息发送测试--------->
android_caps.wd.find_element_by_id("message_ed_msgeditor").send_keys("text")
android_caps.wd.find_element_by_id("message_btn_sendtext").click()
try:
    sleep(5)
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("送达")')
    print("文本消息已送达")
except:
    print("文本消息送达失败")
msgtext = android_caps.wd.find_element_by_id("message_tv_msgtext")
action.long_press(el=msgtext).perform()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("删除消息")').click()
sleep(2)
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("text")').is_displayed()
    print("删除文本消息失败")
except:
    print("删除文本消息成功,进行下一步")
# <---------小表情发送测试--------->
android_caps.wd.find_element_by_id("message_btn_openemotes").click()
android_caps.wd.tap([(252, 1355), (252, 1355)], None)
android_caps.wd.find_element_by_id("message_btn_sendtext").click()
try:
    sleep(5)
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("送达")')
    print("小表情已送达")
except:
    print("小表情送达失败")
action.long_press(el=msgtext).perform()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("删除消息")').click()
sleep(2)
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("[挖鼻孔]")').is_displayed()
    print("删除小表情失败")
except:
    print("删除小表情成功,进行下一步")
# <---------大表情发送测试--------->
android_caps.wd.tap([(645, 1867), (645, 1867)], None)
sleep(3)
android_caps.wd.tap([(177, 1277), (177, 1277)], None)
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("送达")')
    print("大表情已送达")
except:
    print("大表情送达失败")
messgif = android_caps.wd.find_element_by_id("message_gifview")
action.long_press(el=messgif).perform()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("删除消息")').click()
sleep(2)
try:
    android_caps.wd.find_element_by_id("message_gifview").is_displayed()
    print("删除大表情失败")
except:
    print("删除大表情成功,进行下一步")
# <---------语音消息发送测试--------->
android_caps.wd.find_element_by_id("message_btn_gotoaudio").click()
audio_record = android_caps.wd.find_element_by_id("audio_record_button")
action.long_press(el=audio_record).wait(10000).release().perform()
sleep(15)
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("送达")')
    print("语音已送达")
except:
    print("语音送达失败")
android_caps.wd.find_element_by_id("message_layout_audiotopcontent").click()
sleep(3)
try:
    android_caps.wd.find_element_by_id("message_iv_playimage").is_displayed()
    print("语音播放成功")
except:
    print("语音播放失败")
messaudio = android_caps.wd.find_element_by_id("message_layout_audiotopcontent")
action.long_press(el=messaudio).perform()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("删除消息")').click()
sleep(2)
try:
    android_caps.wd.find_element_by_id("message_layout_audiotopcontent").is_displayed()
    print("删除语音失败")
except:
    print("删除语音成功,进行下一步")
# <---------图片发送测试--------->
android_caps.wd.find_element_by_id("message_btn_selectpic").click()
sleep(3)
android_caps.wd.swipe(start_x=497, start_y=1477, end_x=674, end_y=662, duration=4000)
try:
    sleep(5)
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("送达")')
    print("图片已送达")
except:
    print("图片送达失败")
    android_caps.wd.find_element_by_id("message_iv_msgimage").click()
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("下载失败")').is_displayed()
    print("图片加载失败")
except:
    print("图片加载成功")
    android_caps.wd.press_keycode(4)
messimage = android_caps.wd.find_element_by_id("message_iv_msgimage")
action.long_press(el=messimage).perform()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("删除消息")').click()
sleep(2)
try:
    android_caps.wd.find_element_by_id("message_iv_msgimage").is_displayed()
    print("删除图片失败")
except:
    print("删除图片成功,进行下一步")
# <---------地理位置发送测试--------->
android_caps.wd.find_element_by_id("message_btn_location").click()
sleep(8)
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("我的位置")').is_displayed()
    print("默认位置加载成功")
    android_caps.wd.find_element_by_id("menu_map_send").click()
except:
    print("默认位置加载失败")
try:
    sleep(5)
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("送达")')
    print("位置已送达")
except:
    print("位置送达失败")
android_caps.wd.find_element_by_id("message_iv_msgimage").click()
try:
    android_caps.wd.find_element_by_id("btn_navigation").is_displayed()
    print("点击位置消息加载成功")
    sleep(3)
    android_caps.wd.press_keycode(4)
except:
    print("点击位置消息加载失败")
android_caps.wd.find_element_by_id("message_btn_location").click()
sleep(8)
android_caps.wd.tap([(365, 1500), (365, 1500)], None)
try:
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("指定位置")').is_displayed()
    print("指定加载成功")
    android_caps.wd.find_element_by_id("menu_map_send").click()
except:
    print("指定加载失败")
sleep(5)
messbtn = android_caps.wd.find_element_by_id("message_iv_msgimage")
action.long_press(el=messbtn).perform()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("删除消息")').click()
action.long_press(el=messbtn).perform()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("删除消息")').click()
try:
    android_caps.wd.find_element_by_id("message_iv_msgimage").is_displayed()
    print("删除位置失败")
except:
    print("删除位置成功,进行下一步")

# <---------视频发送测试--------->
android_caps.wd.find_element_by_id("message_btn_take_video").click()
android_caps.wd.find_element_by_id("recorder_change_camera").click()
sleep(5)
video_record = android_caps.wd.find_element_by_id("record_button")
action.long_press(el=video_record).wait(10000).release().perform()
sleep(10)
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("完成")').click()
sleep(10)
try:
    sleep(5)
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("送达")')
    print("视频已送达")
except:
    print("视频送达失败")
messvideo = android_caps.wd.find_element_by_id("message_layout_messagecontainer")
action.long_press(el=messvideo).perform()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("删除消息")').click()
try:
    android_caps.wd.find_element_by_id("message_layout_messagecontainer").is_displayed()
    print("删除视频失败")
except:
    print("删除视频成功,进行下一步")

# <---------webapp音乐发送测试--------->
android_caps.wd.find_element_by_id("message_iv_openplus_icon").click()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("音乐")').click()
android_caps.wd.find_element_by_id("toolbar_search_edittext").send_keys("Yesterday Once More")
sleep(5)
android_caps.wd.tap([(468, 323), (468, 323)], None)
android_caps.wd.find_element_by_id("button1").click()
try:
    sleep(5)
    android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("送达")')
    print("音乐已送达")
except:
    print("音乐送达失败")
android_caps.wd.find_element_by_id("iv_music_icon").click()
sleep(5)
android_caps.wd.tap([(928, 1632), (928, 1632)], None)
try:
    android_caps.wd.find_element_by_id("music_playing_topbar").is_displayed()
    print("音乐小窗加载成功")
    android_caps.wd.find_element_by_id("playing_status").click()
    android_caps.wd.press_keycode(4)
except:
    print("音乐小窗加载失败")
messmusic = android_caps.wd.find_element_by_id("tv_music_name")
action.long_press(el=messmusic).perform()
android_caps.wd.find_element_by_android_uiautomator('new UiSelector().text("删除消息")').click()
try:
    android_caps.wd.find_element_by_id("tv_music_name").is_displayed()
    print("删除音乐消息失败")
except:
    print("删除音乐消息成功")

print("单人对话case执行完毕")
sleep(30)
android_caps.wd.quit()