# -*- coding: utf-8 -*-
# @Time : 2023/4/8/008 21:33
# @Author : WuChen
# @File : test.py
# @Software : PyCharm
import re

str1 = "速度过慢if(x1.bit1==1) 速度过快if(x1.bit2==1) 横摆角过大if(x1.bit3==1) 加速过快if(x1.bit4==1) 目标不充分if(x1.bit5==1) 雷达失明if(x1.bit6==1)if(x1.bit7==1)if(x1==0) 正常"
str2 = "速度过慢if(x1.bit1==1) 速度过快if(x1.bit2==1) 横摆角过大if(x1.bit3==1) 加速过快if(x1.bit4==1) 目标不充分if(x1.bit5==1) 雷达失明if(x1.bit6==1)if(x1.bit7==1)if(x1==0) 正常"

aa = re.fullmatch(str1, str2)
print(aa)

str3 = '速度过慢(x1.bit1==1'
str4 = '速度过慢(x1.bit1==1)'

# b = re.fullmatch(str3, str4)
# print(b)

from datetime import datetime

# 获取当前日期和时间
now = datetime.now()

# 格式化日期时间为字符串
date_time_str = now.strftime("%Y-%m-%d %A %w")

# 打印日期时间
print(date_time_str)

