# -*- coding: utf-8 -*-

import android_caps
import xlrd
import random

# 获取resource_id
def get_resource_id(resource_id):
    element = android_caps.self.find_element_by_id(resource_id)
    return element

# 获取class_name
def get_class_name(class_name):
    element = android_caps.self.find_element_by_class_name(class_name)
    return element

# 获取android_uiautomator
def get_uiautomator(uiautomator):
    element = android_caps.self.find_element_by_android_uiautomator(uiautomator)
    return element

# 获取ccessibility_id，常用语web代码
def get_accessibility_id(accessibility_id):
    element = android_caps.self.find_element_by_accessibility_id(accessibility_id)
    return element

# 获取css
def get_css(css):
    element = android_caps.self.find_element_by_css_selector(css)
    return element

# 坐标操作
def refresh_page(start_x, start_y, end_x, end_y, duration):
    element = android_caps.self.swipe(start_x, start_y, end_x, end_y, duration)
    return element

# 随机读取execl中的陌陌id
random_row = random.randint(1, 2)
def read_momoid():
    xls = xlrd.open_workbook('momo_id.xlsx')
    sheet_name = xls.sheet_by_index(0)
    momo_id = int(sheet_name.cell(random_row, 0).value)
    return momo_id

# 随机读取execl中的陌陌password
def read_momo_password():
    xls = xlrd.open_workbook('momo_id.xlsx')
    sheet_name = xls.sheet_by_index(0)
    password = str(sheet_name.cell(random_row, 1).value)
    return password
