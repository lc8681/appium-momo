# -*- coding: utf-8 -*-
import time
import android_caps
import unittest
import HTMLTestRunner
import login

# 测试用例集合
class LoginTest(unittest.TestCase):
    def quit(self):
        android_caps.self.quit()

    def test_login(self):
        login


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(LoginTest('test_login'))
    suite.addTest(LoginTest('test_quanzi_index'))
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