import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame as df
import  csv
import re
#filename = '猫眼评分排名前100的电影.json'
i = 1
results = []
while i:
    url = 'https://ssr1.scrape.center/page/' + str(i)
    i = i + 1
    strhtml = requests.get(url)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    # print(strhtml.text)
    data = soup.select('#index > div:nth-of-type(1) > div.el-col.el-col-18.el-col-offset-3 > div > div > div ')
    for item in data:
        result = {
            'title': item.get_text()
        }
        result=str(result['title']).split('\n')
        while '' in result:
            result.remove('')
        results.append(result)
        # results.append(result.values())
    if i == 11:
        break
for items in results:
    items.remove(' / ')
    if len(items[-2]) < 12:
        items.insert(-1,'null')
    while len(items) != 10:
        items.insert(-4,'null')
# print(results)
# 通过index参数设置行索引，通过columns参数设置列索引
name = ['电影名','Type1','Type2','Type3','Type4','Type5','上映地点','电影时长','上映时间','评分']
test = df(data=results,index=range(1,101), columns = name)
print(test)
test.to_csv(r'maoyan.csv', index=True, header=True,encoding='utf_8_sig')