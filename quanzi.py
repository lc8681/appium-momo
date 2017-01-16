# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from random import choice

print "< 登录流程end,进入圈子start >"
android_caps.self.find_element_by_id("maintab_layout_profile").click()  # 点击个人帧
# check 圈子通知数量
try:
    android_caps.self.find_element_by_id("new_quanzi_bubble").is_displayed()
    quanzi_bubble = android_caps.self.find_element_by_id("new_quanzi_bubble").text
    print "$ 圈子通知数:" + quanzi_bubble
    android_caps.self.find_element_by_id("quanzi_layout").click()  # 点击圈子入口
    sleep(15)
    btn_bubble = android_caps.self.find_element_by_id("group_btn_bubble").text
    if btn_bubble == quanzi_bubble:
        print "$ 个人帧圈子通知数量与圈子内通知数量相同"
        sleep(5)
        android_caps.self.find_element_by_id("group_btn_bubble").click()
        sleep(5)
        try:
            android_caps.self.find_element_by_id("item_layout").is_displayed()
            print "$ 圈子通知展示正确"
            android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
            sleep(3)
        except:
            print "$ 圈子通知展示不正确.."
            android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
            sleep(3)
    else:
        print "$ 个人帧圈子通知数量与圈子内通知数量不相同!!..."
except:
    print "$ 没有圈子通知"
    android_caps.self.find_element_by_id("quanzi_layout").click()  # 点击圈子入口
    sleep(15)
# -------------
# android_caps.self.find_element_by_accessibility_id("AutoQA 圈主 ").click()
# sleep(15)
# ------------
print "< 进入圈子end,创建圈子start >"
android_caps.self.find_element_by_id("group_btn_layout").click()
sleep(10)

# 点击创建圈子按钮
android_caps.self.find_element_by_android_uiautomator(
        'new UiSelector().className("android.view.View").index(3)').click()
try:
    android_caps.self.find_element_by_accessibility_id("1个人只能创建1个圈子，无法创建").is_displayed()
    print "$ 1个人只能创建1个圈子,脚本结束!"
    sleep(5)
    android_caps.self.quit()
except:
    print "$ 满足创建圈子的条件,流程继续..."
android_caps.self.find_element_by_class_name("android.widget.EditText").send_keys("AutoQA")
sleep(3)
android_caps.self.find_element_by_accessibility_id("下一步").click()
sleep(3)
android_caps.self.find_element_by_accessibility_id("添加头像").click()
android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("本地相册")').click()
android_caps.self.find_element_by_android_uiautomator('new UiSelector()'
                                                      '.className("android.widget.RelativeLayout").index(1)').click()
sleep(3)
android_caps.self.find_element_by_id("imagefactory_btn2").click()
sleep(3)
android_caps.self.find_element_by_id("imagefactory_btn2").click()
sleep(3)
android_caps.self.find_element_by_accessibility_id("选择圈子分类 ").click()
android_caps.self.find_element_by_accessibility_id("情感交流 ").click()
sleep(1)
android_caps.self.find_element_by_accessibility_id("下一步").click()
android_caps.self.find_element_by_class_name("android.widget.EditText").send_keys("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
android_caps.self.find_element_by_accessibility_id("完成").click()
sleep(15)
try:
    android_caps.self.find_element_by_accessibility_id("圈子创建成功").is_displayed()
    print "$ 圈子创建成功!"
    android_caps.self.find_element_by_accessibility_id("进入圈子").click()
except:
    print "$ 圈子创建失败!!!"

print "< 创建圈子end,发布帖子start >"
sleep(15)
android_caps.self.find_element_by_accessibility_id("发布帖子").click()
sleep(3)
android_caps.self.find_element_by_id("tv_topic").send_keys("quanzi_test")
android_caps.self.find_element_by_id("signeditor_tv_text").send_keys("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
pic = android_caps.self.find_element_by_id("layout_add_pic")
video = android_caps.self.find_element_by_id("layout_add_video")
ran = [pic, video]
if choice(ran) == video:
    video.click()
    android_caps.self.find_element_by_id("recorder_change_camera").click()
    sleep(3)
    android_caps.self.find_element_by_id("record_button").click()
    sleep(40)
    android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("完成")').click()
    sleep(20)
else:
    choice(ran) == pic
    pic.click()
    android_caps.self.find_element_by_id("checkbox").click()
    sleep(1)
    android_caps.self.find_element_by_id("multpic_main_send").click()
    sleep(2)

android_caps.self.find_element_by_id("layout_site").click()
sleep(5)
android_caps.self.find_element_by_id("site_name").click()
try:
    android_caps.self.find_element_by_id("tv_feed_site_selected").is_displayed()
    print "$ 发布界面地点显示正常"
except:
    print "$ 发布界面地点显示不正常"
android_caps.self.find_element_by_accessibility_id("发布").click()
sleep(10)
try:  # 用"刚刚"来判断是否发布成功
    android_caps.self.find_element_by_accessibility_id("刚刚").is_displayed()
    print "$ 发布成功"
except:
    try:  # 用"1分钟前"来判断是否发布成功
        android_caps.self.find_element_by_accessibility_id("1分钟前").is_displayed()
        print "$ 发帖成功"
    except:
        print "$ 发帖失败"
sleep(3)
print "< 发布帖子end,评论start >"
android_caps.self.find_element_by_accessibility_id("1477308133728-comment").click()
sleep(3)
# 图片和文字评论随机发
comment_pic = android_caps.self.find_element_by_id("layout_select_pic")
comment_text = android_caps.self.find_element_by_id("message_ed_msgeditor")
ran = [comment_pic, comment_text]
if choice(ran) == comment_pic:
    comment_pic.click()
    android_caps.self.find_element_by_id("checkbox").click()
    sleep(3)
    android_caps.self.find_element_by_id("multpic_main_send").click()
    sleep(3)
    print "$ 添加" + android_caps.self.find_element_by_id("pic_number_bubble").text + "张图片"
    android_caps.self.find_element_by_id("message_btn_sendtext").click()
    sleep(5)

else:
    choice(ran) == comment_text
    comment_text.send_keys("No.1")
    android_caps.self.find_element_by_id("message_btn_sendtext").click()
    sleep(2)
# android_caps.self.swipe(start_x=534, start_y=1534, end_x=534, end_y=415, duration=None)  # 滚动页面
try:
    android_caps.self.find_element_by_accessibility_id("sonny刚刚 · 2楼").is_displayed()
    print "$ 评论成功"
except:
    try:
        android_caps.self.find_element_by_accessibility_id("sonny1分钟前 · 2楼").is_displayed()
        print "$ 评论成功"
    except:
        print "$ 评论失败!"
# android_caps.self.swipe(start_x=534, start_y=1534, end_x=534, end_y=415, duration=None)   # 滚动页面
# 删除评论
android_caps.self.find_element_by_accessibility_id("more-test").click()
android_caps.self.find_element_by_accessibility_id("删除评论").click()
sleep(3)
android_caps.self.find_element_by_accessibility_id("确定").click()
sleep(3)
try:
    android_caps.self.find_element_by_accessibility_id("more-test").is_displayed()
    print "$ 删除评论失败!"
except:
    print "$ 删除评论成功"
print "< 评论end,点赞start >"
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
sleep(3)
android_caps.self.find_element_by_accessibility_id("like").click()  # 点赞
try:
    android_caps.self.find_element_by_accessibility_id("liked").is_displayed()
    print "$ 点赞成功"
except:
    print "$ 点赞失败!"
print "< 点赞end,分享start >"
android_caps.self.find_element_by_accessibility_id("1479361325382-share").click()
try:
    android_caps.self.find_element_by_id("alertTitle").is_displayed()
    print "$ 分享框正确弹出"
    feed_share = android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("动态")')
    group_share = android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("好友/群组")')
    ran = [feed_share, group_share]
    if choice(ran) == feed_share:
        feed_share.click()
        android_caps.self.find_element_by_id("signeditor_tv_text").send_keys("Test")
        android_caps.self.find_element_by_accessibility_id("保存").click()
        sleep(5)

    else:
        choice(ran) == group_share
        group_share.click()
        android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("全部好友")').click()
        android_caps.self.find_element_by_accessibility_id("搜索").click()
        android_caps.self.find_element_by_id("toolbar_search_edittext").send_keys("173489501")
        sleep(5)
        android_caps.self.find_element_by_id("userlist_item_tv_name").click()
        android_caps.self.find_element_by_id("button1").click()
        sleep(5)
except:
    print "$ 没有弹出分享框!"
print "< 分享end,操作帖子start >"

# 加精
print "$ 设置精华..."
android_caps.self.find_element_by_accessibility_id("more").click()
android_caps.self.find_element_by_accessibility_id("帖子加精").click()
android_caps.self.find_element_by_accessibility_id("确定").click()
sleep(10)
android_caps.self.swipe(start_x=700, start_y=770, end_x=700, end_y=2000, duration=500)
sleep(5)
android_caps.self.find_element_by_accessibility_id("热门").click()
sleep(3)
android_caps.self.swipe(start_x=700, start_y=770, end_x=700, end_y=2000, duration=500)
# check群组tab是否有数据
try:
    android_caps.self.find_element_by_accessibility_id("liked").is_displayed()
    print "$ 设置精华成功"
except:
    print "$ 设置精华失败"
sleep(5)
android_caps.self.find_element_by_accessibility_id("最新").click()
# 置顶
print "$ 设置置顶..."
android_caps.self.find_element_by_accessibility_id("more").click()
android_caps.self.find_element_by_accessibility_id("帖子置顶").click()
android_caps.self.find_element_by_accessibility_id("确定").click()
sleep(10)
android_caps.self.swipe(start_x=700, start_y=770, end_x=700, end_y=2000, duration=500)
sleep(5)
try:
    android_caps.self.find_element_by_accessibility_id("1477971539516-top").is_displayed()
    print "$ 置顶设置成功"
except:
    print "$ 置顶设置失败"
sleep(10)
print "< 操作帖子end,群组tab操作start >"
android_caps.self.find_element_by_accessibility_id("群组").click()
sleep(3)
# 添加圈子群组
android_caps.self.find_element_by_accessibility_id("添加群组").click()
sleep(10)
android_caps.self.find_element_by_class_name("android.widget.EditText").click()
sleep(3)
android_caps.self.find_element_by_class_name("android.widget.EditText").send_keys("34805293")
sleep(10)
try:
    android_caps.self.find_element_by_accessibility_id("添加").is_displayed()
    print "$ 搜索群组正确"
except:
    print "$ 没有搜索到群组,测试结束..."
    android_caps.self.quit()
# check添加
android_caps.self.find_element_by_accessibility_id("添加").click()
try:
    android_caps.self.find_element_by_accessibility_id("已添加").is_displayed()
    print "$ 添加群组成功"
except:
    print "$ 添加群组失败..."

# 添加未加入群组
sleep(3)
android_caps.self.find_element_by_class_name("android.widget.EditText").click()
sleep(3)
android_caps.self.find_element_by_class_name("android.widget.EditText").clear()
sleep(3)
android_caps.self.find_element_by_class_name("android.widget.EditText").send_keys("15649776")
sleep(10)
try:
    android_caps.self.find_element_by_accessibility_id("添加").is_displayed()
    print "$ 搜索群组正确"
except:
    print "$ 没有搜索到群组,测试结束..."
    android_caps.self.quit()
# check添加
android_caps.self.find_element_by_accessibility_id("添加").click()
try:
    android_caps.self.find_element_by_accessibility_id("已添加").is_displayed()
    print "$ 添加群组成功"
except:
    print "$ 添加群组失败..."
# check 群组tab是否有数据(已加入的群组)
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
sleep(2)
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
android_caps.self.swipe(start_x=700, start_y=770, end_x=700, end_y=2000, duration=500)
sleep(5)
try:
    android_caps.self.find_element_by_accessibility_id("已加入").is_displayed()
    print "$ 群组tab—已加入群组展示正确"
except:
    print "$ 群组tab—已加入群组展示失败..."
# check 群组tab是否有数据(未加入的群组)
try:
    android_caps.self.find_element_by_accessibility_id("加入").is_displayed()
    print "$ 群组tab—未加入群组展示正确"
    # 点击加入按钮
    android_caps.self.find_element_by_accessibility_id("加入").click()
    sleep(10)
    try:
        android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("申请加入群组")').is_displayed()
        print "$ 申请加入群组页面进入成功"
        print "$ " + android_caps.self.find_element_by_id("person_group_information").text
        android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
    except:
        print "$ 申请加入群组页面进入失败,测试流程结束"
        android_caps.self.quit()
except:
    print "$ 群组tab—未加入群组展示失败..."

print "< 群组tab操作end,圈子资料start >"
android_caps.self.find_element_by_id("toolbar_single_menu_id").click()
sleep(15)
# 管理员
android_caps.self.find_element_by_android_uiautomator(
        'new UiSelector().className("android.view.View").index(9)').click()
manager = android_caps.self.find_element_by_id("web_title_textview").text
if manager == "圈子管理员":
    print "$ 圈子管理员页面载入正确"
    android_caps.self.find_element_by_class_name("android.widget.EditText").click()
    sleep(2)
    android_caps.self.find_element_by_class_name("android.widget.EditText").send_keys("173489501")
    try:
        android_caps.self.find_element_by_accessibility_id("任命").is_displayed()
        print "$ 管理员搜索结果展示正确"
    except:
        print "$ 管理员搜索结果展示不正确"
else:
    print "$ 圈子管理员页面载入异常"
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
sleep(2)
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
sleep(2)
# 精华帖
android_caps.self.find_element_by_accessibility_id("精华帖").click()
sleep(5)
try:
    android_caps.self.find_element_by_accessibility_id("1477308133728-comment").is_displayed()
    print "$ 精华帖展示正确"
except:
    print "$ 精华帖展示不正确!"
sleep(2)
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
sleep(2)
# 我的圈内等级
android_caps.self.find_element_by_accessibility_id("我的圈内等级孤独求败").click()
level = android_caps.self.find_element_by_id("web_title_textview").text
if level == "圈子成员等级":
    print "$ 圈子成员等级页面载入正确"
    sleep(10)
    android_caps.self.find_element_by_accessibility_id("称号模板").click()
    sleep(2)
    try:
        android_caps.self.find_element_by_accessibility_id("选择模板").is_displayed()
        print "$ 成员等级模板弹出正常"
        android_caps.self.find_element_by_accessibility_id("成就").click()
        sleep(2)
        try:
            android_caps.self.find_element_by_accessibility_id("选择模板").is_displayed()
            print "$ 成就选择失败!"
        except:
            print "$ 成就选择正确!"
    except:
        print "$ 成员等级模板弹出不正常"
else:
    print "$ 圈子成员等级页面载入异常"

sleep(5)
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
sleep(20)
# 添加友情圈子
android_caps.self.swipe(start_x=534, start_y=1534, end_x=534, end_y=415, duration=None)
sleep(3)
android_caps.self.find_element_by_accessibility_id("添加").click()
sleep(15)
friendship = android_caps.self.find_element_by_id("web_title_textview").text
if friendship == "友情圈子":
    print "$ 友情圈子页面载入正确"
    android_caps.self.find_element_by_class_name("android.widget.EditText").click()
    sleep(2)
    android_caps.self.find_element_by_class_name("android.widget.EditText").send_keys("mmqa")
    sleep(5)
    try:
        android_caps.self.find_element_by_accessibility_id("添加").is_displayed()
        print "$ 友情圈子搜索正确!"
        sleep(2)
        android_caps.self.find_element_by_accessibility_id("添加").click()
        sleep(5)
        android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
        sleep(3)
        try:
            android_caps.self.find_element_by_accessibility_id("删除").is_displayed()
            print "$ 添加友情圈子成功"
        except:
            print "$ 添加友情圈子失败!"
    except:
        print "$ 友情圈子搜索错误!"

else:
    print "$ 友情圈子页面载入异常!"
sleep(3)
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
sleep(3)
try:
    android_caps.self.find_element_by_accessibility_id("mmqa").is_displayed()
    print "$ 友情圈子资料页展示正确"
except:
    print "$ 友情圈子资料页展示失败!"
# 删除友情圈子
android_caps.self.find_element_by_accessibility_id("添加").click()
sleep(10)
android_caps.self.find_element_by_accessibility_id("删除").click()
sleep(3)
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
sleep(5)
try:
    android_caps.self.find_element_by_accessibility_id("mmqa").is_displayed()
    print "$ 友情圈子删除失败"
except:
    print "$ 友情圈子删除正确!"
sleep(3)
# 编辑圈子
android_caps.self.find_element_by_accessibility_id(" 编辑圈子").click()
sleep(3)
edit = android_caps.self.find_element_by_id("web_title_textview").text
if edit == "圈子资料":
    print "$ 编辑圈子页面载入正确"
else:
    print "$ 编辑圈子页面载入异常!"
sleep(2)
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
sleep(3)
# 分享圈子
android_caps.self.find_element_by_accessibility_id(" 分享圈子").click()
sleep(2)
try:
    android_caps.self.find_element_by_id("alertTitle").is_displayed()
    print "$ 分享框正确弹出"
    feed_share = android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("动态")')
    group_share = android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("好友/群组")')
    ran = [feed_share, group_share]
    if choice(ran) == feed_share:
        feed_share.click()
        android_caps.self.find_element_by_id("signeditor_tv_text").send_keys("Test")
        android_caps.self.find_element_by_accessibility_id("保存").click()
        sleep(5)

    else:
        choice(ran) == group_share
        group_share.click()
        android_caps.self.find_element_by_android_uiautomator('new UiSelector().text("全部好友")').click()
        android_caps.self.find_element_by_accessibility_id("搜索").click()
        android_caps.self.find_element_by_id("toolbar_search_edittext").send_keys("173489501")
        sleep(5)
        android_caps.self.find_element_by_id("userlist_item_tv_name").click()
        android_caps.self.find_element_by_id("button1").click()
        sleep(5)
except:
    print "$ 没有弹出分享框!"
print "< 圈子资料end,退出圈子start >"
android_caps.self.find_element_by_accessibility_id("退出圈子").click()
sleep(3)
try:
    android_caps.self.find_element_by_accessibility_id("提示").is_displayed()
    print "$ 确认框弹出正常"
    sleep(3)
    android_caps.self.find_element_by_accessibility_id("确定").click()
    sleep(5)
except:
    print "$ 确认框弹出失败,测试终止..."
    android_caps.self.quit()
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
try:
    android_caps.self.find_element_by_accessibility_id("AutoQA 圈主 ").is_displayed()
    print "$ 圈子退出失败!..."
except:
    print "$ 圈子退出成功..."
sleep(5)
print "< 退出圈子end,我的帖子start >"
android_caps.self.find_element_by_accessibility_id("我的帖子").click()
sleep(3)
android_caps.self.swipe(start_x=534, start_y=1534, end_x=534, end_y=415, duration=None)
sleep(3)
try:
    android_caps.self.find_element_by_accessibility_id("more").is_displayed()
    android_caps.self.find_element_by_accessibility_id("1477308133728-comment").is_displayed()
    android_caps.self.find_element_by_accessibility_id("1479361325382-share").is_displayed()
    print "$ 发布tab各功能元素展示正确"
except:
    print "$ 发布tab元素展示异常!"
sleep(3)
android_caps.self.find_element_by_accessibility_id("评论").click()
sleep(3)
android_caps.self.swipe(start_x=534, start_y=1534, end_x=534, end_y=415, duration=None)
sleep(3)
try:
    android_caps.self.find_element_by_accessibility_id("more").is_displayed()
    android_caps.self.find_element_by_accessibility_id("1477308133728-comment").is_displayed()
    android_caps.self.find_element_by_accessibility_id("1479361325382-share").is_displayed()
    print "$ 评论tab各功能元素展示正确"
except:
    print "$ 评论tab元素展示异常!"
sleep(3)
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
sleep(3)
print "< 我的帖子end,我的圈子start >"
# 查看全部
android_caps.self.find_element_by_accessibility_id("查看全部 ").click()
sleep(10)
try:
    android_caps.self.find_element_by_accessibility_id("mmqa圈主").is_displayed()
    print "$ 我的圈子页面加载正确"
except:
    print "$ 我的圈子页面加载异常!"
sleep(5)
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
sleep(3)
# 添加
android_caps.self.find_element_by_accessibility_id(" 添加").click()
sleep(5)
try:
    android_caps.self.find_element_by_accessibility_id("最新").is_displayed()
    android_caps.self.find_element_by_class_name("android.widget.EditText").click()
    sleep(2)
    android_caps.self.find_element_by_accessibility_id("情感交流").is_displayed()
    print "$ 添加圈子页面数据显示正确"
except:
    print "$ 添加圈子页面数据显示异常!"
sleep(3)
android_caps.self.find_element_by_accessibility_id("取消").click()
sleep(3)
android_caps.self.find_element_by_class_name("android.widget.ImageButton").click()
sleep(5)
# 校验最新帖子数据是否展示正常
try:
    android_caps.self.find_element_by_accessibility_id("最新帖子").is_displayed()
    print "$ 最新帖子数据显示正确"
except:
    print "$ 最新帖子数据显示异常!"
sleep(5)
print "< 所有流程结束...>"
android_caps.self.quit()
