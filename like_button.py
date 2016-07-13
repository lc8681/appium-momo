# -*- coding: utf-8 -*-
# python学习，加油！
import android_caps
from time import sleep
if android_caps.wd.find_element_by_id("nearby_match_lik").is_displayed():
    print("True")

else:
    print("False")

sleep(5)
android_caps.wd.quit()
