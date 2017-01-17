# -*- coding: utf-8 -*-
# python学习，加油！
import time
import unittest

import HTMLTestRunner
import android_caps
import login


# 测试用例集合
class LoginTest(unittest.TestCase):
    def quit(cls):
        android_caps.self.quit()

    def test_login(self):
        login
'''
    def test_quanzi_index(self):
        quanzi_index
'''

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginTest('test_login'))
   # suite.addTest(LoginTest('test_quanzi_index'))
    timestr = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
    filename = 'Test report' + '(' + timestr + ')' + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='result',
            description='report'
    )
    runner.run(suite)
    fp.close()
