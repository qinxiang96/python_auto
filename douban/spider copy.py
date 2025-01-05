#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   spider.py
@Time    :   2025/01/05 14:10:35
@Author  :   qinxiang 
@Version :   1.0
@Site    :   https://github.com/qinxiang96
@Desc    :   None
'''
import urllib.request
from bs4 import BeautifulSoup
import re
import xlwt


def main():
    base_url = "https://movie.douban.com/top250?start="
    #askURL(base_url)
    # 1、爬取网页
    dataList = getData(base_url)
    savePath = "豆瓣电影TOP250.xls"
    # saveData(dataList,savePath)

    # 2、解析数据
    
    # 3、保存数据
# 创建正则表达式对象，表示规则（字符串的模式）
# 影片链接
findLink = re.compile(r'<a href="(.*?)">')
#影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S) #re.S表示忽略换行符，让换行符包含在字符中
#影片片名
findTitle = re.compile(r'<span class="title">(.*?)</span>')

# 得到指定一个URL的网页内容
def askURL(url):
    # 用户代理：表示告诉豆瓣服务器，我们是什么类型的机器，浏览器
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

    }
    req = urllib.request.Request(url=url,headers=headers)
    html = ""

    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        # print(html)
    except Exception as e:
        print(e)
    return html

# 1、爬取网页
def getData(base_url):
    datalist = []
    for i in range(0,10):
        url = base_url +str(i*25)
        html = askURL(url)
        # 2、解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            data = []
            item = str(item) # 查找符合要求的数据，形成列表
            link = re.findall(findLink,item)[0]
            data.append(link)
            title = re.findall(findTitle,item)
            if(len(title) == 2):
                ctitle = title[0]
                data.append(ctitle)
                otitle = title[1].replace("\xa0/\xa0","")
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(' ')
            datalist.append(data)
    print(datalist)
            
    return datalist

# 3、保存数据
def saveData(datalist,savepath):
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    worksheet.write(0,0,'hello')
    workcol = ("链接","中文片名","外文片名")
    for i  in range(0,3):
        worksheet.write(0,i,workcol[i])
    for i in range(0,250):
        data = datalist[i]
        for j in range(0,3):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)
    return 0
if __name__ == "__main__":# 当程序执行时
    # 调用函数
    main()