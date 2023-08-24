#!/usr/bin/env python3

import json

stickers = ['[微笑]','[撇嘴]','[色]','[发呆]','[得意]','[流泪]','[害羞]','[闭嘴]','[睡]','[大哭]','[尴尬]','[发怒]','[调皮]','[呲牙]','[惊讶]','[难过]','[囧]','[抓狂]','[吐]','[偷笑]','[愉快]','[白眼]','[傲慢]','[困]','[惊恐]','[憨笑]','[悠闲]','[咒骂]','[疑问]','[嘘]','[晕]','[衰]','[骷髅]','[敲打]','[再见]','[擦汗]','[抠鼻]','[鼓掌]','[坏笑]','[右哼哼]','[鄙视]','[委屈]','[快哭了]','[阴险]','[亲亲]','[可怜]','[笑脸]','[生病]','[脸红]','[破涕为笑]','[恐惧]','[失望]','[无语]','[嘿哈]','[捂脸]','[奸笑]','[机智]','[皱眉]','[耶]','[吃瓜]','[加油]','[汗]','[天啊]','[Emm]','[社会社会]','[旺柴]','[好的]','[打脸]','[哇]','[翻白眼]','[666]','[让我看看]','[叹气]','[苦涩]','[裂开]','[嘴唇]','[爱心]','[心碎]','[拥抱]','[强]','[弱]','[握手]','[胜利]','[抱拳]','[勾引]','[拳头]','[OK]','[合十]','[啤酒]','[咖啡]','[蛋糕]','[玫瑰]','[凋谢]','[菜刀]','[炸弹]','[便便]','[月亮]','[太阳]','[庆祝]','[礼物]','[红包]','[發]','[福]','[烟花]','[爆竹]','[猪头]','[跳跳]','[发抖]','[转圈]']
stickers_dict = {stickers: 0 for stickers in stickers}

data = open('/Users/james/Desktop/WeChatDB/db2/Chat_3c0825dcf3b568028bcf00ee45656d60.json')
data = data.read()
data = json.loads(data)

for item in data:
    for word in stickers_dict.keys():
        stickers_dict[word] += item['msgContent'].count(word)

# 剔除计数为 0 的表情
data = {key: value for key, value in stickers_dict.items() if value != 0}

import pandas as pd
# 使用 DataFrame.from_dict() 将字典转换为 DataFrame
df = pd.DataFrame.from_dict(data, orient='index', columns=['数量'])

# 添加表情列
df['表情'] = df.index

# 按数量降序排序
df = df.sort_values(by='数量', ascending=False)

# 重置索引
df = df[['表情', '数量']]
df = df.reset_index(drop=True)

# 保存 DataFrame 到 CSV 文件（不包括标题行）
df.to_excel('~/Desktop/emoji_data.xlsx', index=False)

print("数据已保存到 ~/Desktop/emoji_data.xlsx 文件中。")
