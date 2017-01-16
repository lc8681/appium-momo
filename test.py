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
        print "login pass"

    def test_login(self):
        login_again = True
        while login_again:
            try:
                main.get_resource_id("login_et_momoid").is_displayed()
                def username_clear(text):
                    android_caps.self.keyevent(123)
                    for i in range(0, len(text)):
                        android_caps.self.keyevent(67)
                adr = android_caps.self.find_element_by_id("login_et_momoid")
                adr.click()
                context2 = adr.get_attribute('text')
                username_clear(context2)

                username = adr.send_keys()
                android_caps.self.find_element_by_id("login_et_momoid").send_keys(username)  # 输入用户名
                android_caps.self.find_element_by_id("login_et_pself").click()
                sleep(1)
                android_caps.self.press_keycode(67)    # 删除键(方法太TM的笨了..但是又想不到新方法,因为密码框没有text属性,所以不能和用户名一样处理)
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

                password = raw_input("请输入密码:")
                android_caps.self.find_element_by_id("login_et_pself").send_keys(password)     # 输入密码
                android_caps.self.find_element_by_id("btn_ok").click()   # 确定登录
                sleep(5)
                try:
                    android_caps.self.find_element_by_id("nearby_match_like").is_displayed()
                    login_again = False
                except:
                    print ("用户名或密码错误,正在重启登录流程....")
                    android_caps.self.find_element_by_id("button2").click()

            except:
                print ("用户名或密码错误,正在重启登录流程....")
                android_caps.self.find_element_by_id("button2").click()

        print("登录成功")

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginTest('test_goto_login'))
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
