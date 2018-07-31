# encoding = utf-8
import requests
import json
import jieba
from pandas import DataFrame
import pandas as pd
import numpy as np

def getnews(pages):
    global newsbag
    newsbag = []
    for page in range(1, pages + 1):
        raw_url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=10&show_num=100&tag=1&format=json&page={}&callback=newsloadercallback&_=1487824946231'
        url = raw_url.format(page)
        res = requests.get(url)
        jd = json.loads(res.text.lstrip(' newsloadercallback(').rstrip(');'))
        diclist = jd['result']['data']
        for ent in diclist:
            newsbag.append(ent['title'])
        continue
    return newsbag


def cutseg():
    global seg_list
    seg_list = []
    title_list = []
    for i in newsbag:
        title_list = list(jieba.cut(i))
        seg_list = seg_list + title_list

    return seg_list


print('欢迎使用新浪国内新闻标题分词！')
pages = int(input("你想查询（返回输入值的10倍）："))
getnews(pages)
cutseg()
local_list = []
newslocal_list = []

# 载入地名词典
with open('D:\local.txt', 'r', encoding='utf-8') as reader:
    for local in reader.readlines():
        local = local.strip('\n')
        local_list.append(local)
    reader.close()
for i in seg_list:
    if  i in local_list :
        newslocal_list.append(i)
    else:
        continue

#统计频次并输出
local_set = ()
count_local_list = []
final_count_local = []
local_set = set(newslocal_list)

for local in local_set:
    count_local_list.append(newslocal_list.count(local))
final_count_local = list(zip(local_set,count_local_list))
dataNumPy = np.asarray(final_count_local)
DF1 = pd.DataFrame(dataNumPy,columns=['地名','出现次数'])
DF1.to_excel('3000条.xlsx')
print('Done!')