#!/usr/bin/env python3
import os
import json
import datetime
import numpy as np
import matplotlib.pyplot as plt
from mplfonts import use_font
# 导入 SimHei 字体，第一次使用请在项目目录中使用如下命令导入
# mplfonts init && mplfonts install --update SimHei.ttf
use_font('SimHei')

data = open('/Users/james/Code/Chat_a3e8d75a6b1d3cc92d0bdc4dd75efa14.json').read()
data = json.loads(data)

statistics_dict = {}
for item in data:
	unixtime = item.get('msgCreateTime')
	if isinstance(unixtime, int):
		# key 格式：年份.周
		week = int(datetime.datetime.fromtimestamp(unixtime).strftime('%Y%W')) + 1
		if statistics_dict.get(week) is None:
			# 初始化这周的数据为全 0
			statistics_dict[week] = [0, 0, 0, 0, 0, 0, 0]
		# 对应的天数 +1
		day = int(datetime.datetime.fromtimestamp(unixtime).strftime('%w'))
		statistics_dict[week][day] = statistics_dict[week][day] + 1
		
# 对数据结果进行排序
sort = sorted(statistics_dict.items(), key=lambda x:x[0])
values = []
y_labels = []
for item in sort:	
	values.append(item[1])
	y_labels.append(item[0])
x_labels = [ "周日", "周一", "周二", "周三", "周四", "周五", "周六"]

fig, axe = plt.subplots(figsize = (15, 150))
axe.set_xticks(np.arange(len(x_labels)))
axe.set_yticks(np.arange(len(y_labels)))
axe.set_xticklabels(x_labels)
axe.set_yticklabels(y_labels)
im = axe.imshow(values, cmap=plt.cm.Wistia)

# 添加数值标签
for i in range(len(y_labels)):
    for j in range(len(x_labels)):
        axe.text(j, i, values[i][j], ha="center", va="center", color="black")

axe.figure.colorbar(im, ax=axe)
plt.savefig('history.png')