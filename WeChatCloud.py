import os
import json

data = open('/Users/james/Desktop/WeChatDB/db8/Chat_c361fce587751cedffb3e34d40fddb6b.json').read()
data = json.loads(data)

content = ""
for item in data:
    if (item['messageType'] == 1):
        message = item['msgContent'].split('\n')
        if len(message) > 1:
            content += " ".join(message[1:])+ "\n"
        else:
            content += message[0] + "\n"

# 引入结巴分词，对群聊记录进行分词
import jieba
ls = jieba.lcut(content)
# 如果分词出来只有一个字符剔除这个字符
ls = [i for i in ls if len(i) > 1]
text = ' '.join(ls)

# 引入词云
import wordcloud
# 引入停止词模块
from wordcloud import WordCloud, STOPWORDS


stopwords = STOPWORDS
# 添加新的停止词
stopwords.update(['微笑','撇嘴','色','发呆','得意','流泪','害羞','闭嘴','睡','大哭','尴尬','发怒','调皮','呲牙','惊讶','难过','囧','抓狂','吐','偷笑','愉快','白眼','傲慢','困','惊恐','憨笑','悠闲','咒骂','疑问','嘘','晕','衰','骷髅','敲打','再见','擦汗','抠鼻','鼓掌','坏笑','右哼哼','鄙视','委屈','快哭了','阴险','亲亲','可怜','笑脸','生病','脸红','破涕为笑','恐惧','失望','无语','嘿哈','捂脸','奸笑','机智','皱眉','耶','吃瓜','加油','汗','天啊','Emm','社会社会','旺柴','好的','打脸','哇','翻白眼','666','让我看看','叹气','苦涩','裂开','嘴唇','爱心','心碎','拥抱','强','弱','握手','胜利','抱拳','勾引','拳头','OK','合十','啤酒','咖啡','蛋糕','玫瑰','凋谢','菜刀','炸弹','便便','月亮','太阳','庆祝','礼物','红包','發','福','烟花','爆竹','猪头','跳跳','发抖','转圈'])

# 引入 imageio 读取爱心图片文件
from imageio.v2 import imread
# 读取爱心图片文件并赋值给 background 变量
background = imread('heart.png')

wc = wordcloud.WordCloud(
    font_path="SIMSUN.ttf",
    width=1000,
    height=1000,
    background_color="skyblue",
    max_words=200,
    # 配置停止词参数
    stopwords=stopwords,
    mask=background
)

wc.generate(text)
wc.to_file("resultHeart.png")