#!/usr/bin/env python3
import os
import json
import datetime

data = open('/Users/james/Desktop/WeChatDB/db2/Chat_3c0825dcf3b568028bcf00ee45656d60.json').read()
data = json.loads(data)

dict = {}
for item in data:
    # 获取消息发送时间
    unixtime = (item['msgCreateTime'])
    if isinstance(unixtime, int):
        value = datetime.datetime.fromtimestamp(unixtime).strftime('%H:%M')
        # 如果分钟数小于 30 则把后两位变成 00
    if int(value[3:]) < 30:
        value = value[:2]+'00'
        # 如果分钟数大于 30 则把后两位变成 30
    else:
        value = value[:2]+'30'
        # 如果存在这个时间点就把计数 +1
    if dict.get(value) is not None:
        dict[value] = dict.get(value)+1
        # 如果不存在这个时间点就初始化计数 = 1
    else:
        dict[value] = 1

# 开始对 dict 时刻分区结果排序
sort_result = sorted(dict.items(), key=lambda x:x[0])
# 存储排序之后的结果
result = {}
for item in sort_result:
    result[item[0]] = item[1]


import matplotlib.pyplot as plt

# 导入字体管理模块
from mplfonts import use_font
#指定中文字体
use_font('SimHei')

axis_x=[i[:2]+'\n点\n'+i[2:] for i in result]
axis_y=[result[i] for i in result]

plt.bar(axis_x,axis_y)
plt.xlabel("时间段")
plt.ylabel("消息数量")
plt.title("蓝翼运动大众群")
plt.show()