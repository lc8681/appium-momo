# -*- coding: utf-8 -*-
# python学习，加油！
from time import sleep
import unittest
import main
import android_caps
import HTMLTestRunner
import time

class LoginTest(unittest.TestCase):
    def quit(cls):
        android_caps.self.quit()
        print "测试结束"

    def test_goto_login(self):
        # 点击个人帧
        sleep(3)
        main.get_resource_id("maintab_layout_profile").click()
        sleep(1)
        # 点击登录按钮
        main.get_resource_id("visitor_btn_login").click()
        print "goto_login pass"

    def test_login(self):
        momoid = main.get_resource_id("login_et_momoid")
        mmpassword = main.get_resource_id("login_et_pwd")
        def username_clear(text):
            android_caps.self.keyevent(123)
            for i in range(0, len(text)):
                android_caps.self.keyevent(67)

        momoid.click()
        context2 = momoid.get_attribute('text')
        username_clear(context2)

        username = main.read_momoid()
        # 输入用户名
        momoid.send_keys(username)

        mmpassword.click()
        sleep(1)
        android_caps.self.press_keycode(67)    # 删除键(方法太笨了..但是又想不到新方法,因为密码框没有text属性,所以不能和用户名一样处理)
        android_caps.self.press_keycode(67)    # 67是keycode键值的回退删除
        android_caps.self.press_keycode(67)
        android_caps.self.press_keycode(67)
        android_caps.self.press_keycode(67)
        android_caps.self.press_keycode(67)
        android_caps.self.press_keycode(67)
        android_caps.self.press_keycode(67)
        android_caps.self.press_keycode(67)
        android_caps.self.press_keycode(67)
        android_caps.self.press_keycode(67)

        password = main.read_momo_password()
        mmpassword.send_keys(password)     # 输入密码
        main.get_resource_id("btn_ok").click()  # 确定登录
        sleep(5)
        try:
            main.get_resource_id("like_match_bg_layout").is_displayed()
            print "login pass"
        except:
            try:
                main.get_resource_id("nearby_match_like").is_displayed()
                print "login pass"
            except:
                print "login fail"
                android_caps.self.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginTest('test_goto_login'))
    suite.addTest(LoginTest('test_login'))
    timestr = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
    filename ='Test report'+'('+timestr+')'+'.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='result',
        description='report'
    )
    runner.run(suite)
    fp.close()
