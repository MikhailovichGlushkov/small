'''
  主要思路：先把每个专业排名对应的学校联系起来，构成一个字典数据结构，再把这些
  分专业的数据结构拿出来，进行去重，拼接处理，整理成为一个二维列表，再对excel进行写入
'''
import time  # 使用time.sleep() 防止反爬程序阻碍爬虫

import requests  # 请求网页源码模块

import bs4

from bs4 import BeautifulSoup

import re  # 正则匹配用库

import numpy as np

import pandas as pd
import pickle

# 使用pikle库把变量存在磁盘上减少内存开销

import sys
	
sys.setrecursionlimit(100000000)  #设置最大递归深度为

major_code = ["0101", "0201", "0202", "0301", "0302", "0303", "0304", "0305",
              "0401", "0402", "0403", "0501", "0502", "0503", "0601", "0602", "0603"]
# 储存所有参评专业的代码；
major = []  # 所有参评专业


def set_link():  # 实现构成不同专业的网页链接
    url_list = []
    for each in major_code:
        url_list.append(
            "http://www.cdgdc.edu.cn/webrms/pages/Ranking/xkpmGXZJ2016.jsp?yjxkdm="+each+"&xkdm=01,02,03,04,05,06")
    return url_list


url = set_link()


def test(ur_s):
    try:
        r = requests.get(ur_s, timeout=500)
        r.raise_for_status()  # 如果状态码不是200，产生异常
        # r.encoding = 'utf-8'     #字符编码格式改成 utf-8
        print("成功")
    except:
        test(ur_s)
        # 异常处理


def getHTMLText(url_op):  # 获取网页源码函数
    try:
        r = requests.get(url_op, timeout=30)
        r.raise_for_status()  # 如果状态码不是200，产生异常
        # r.encoding = 'utf-8'     #字符编码格式改成 utf-8
        print("获取数据表成功系统正在处理.......")
        return r.text
    except:
        print("error")
        getHTMLText(url_op)


def findall_chinese(s):
    '''
    查找字符串中的所有汉字，返回列表
    :param s: 待查找字符串
    :return: list
    '''
    return re.compile('[\u4e00-\u9fff]+').findall(s)[0]


def get_useable_table(link):    # 分析源码获得dict
    text = getHTMLText(link)  # 第0张源码  #对应哲学那张表格
    soup = BeautifulSoup(text)
    table = soup.findAll(bgcolor="#c2d8e5")
    soup_0 = BeautifulSoup(str(table))
    layer = soup_0.findAll('td', string=re.compile("^[A-Z]"))
    college = soup_0.findAll("td", string=re.compile("[大学|学院]"))
    coll_str = []
    layer_str = []
    lay_rowspan = []
    for l in layer:
        layer_str.append(l.string)
        try:
            lay_rowspan.append(l["rowspan"])  # 突破点:获得合并表格的项
        except:
            lay_rowspan.append("1")
    for c in college:
        coll_str.append((findall_chinese(c.string)))
    '''
    下面这一段通过列表 coll_str layer_str lay_rowspan 将合并表格变成一个完整的数据表
  '''
    table_list = []
    j = 0
    for index in range(len(lay_rowspan)):
        i = 1
        while(i <= int(lay_rowspan[index])):
            table_ele = []
            i = i+1
            table_ele.append(coll_str[j])
            j = j+1
            table_ele.append(layer_str[index])
            table_list.append(table_ele)
    return table_list


def get_all_table(uu):  # 获得所有表
    all_table = []
    for u in uu:
        time.sleep(1)
        all_table.append(get_useable_table(u))
    return all_table



""" 
    由于数据量整体来说比较大，所以需要把变量放在磁盘上以增加程序稳定

"""


def save_table_in_disk(usst):
    ou=open("save.pkl", "wb")
    pickle.dump(usst,ou)
    ou.close()


def load_table_in_disk():
  out = open('save.pkl','rb')
  using_table_on_disk = pickle.load(out)
  return using_table_on_disk

""" table=get_all_table(url)

save_table_in_disk(table)"""

using_table=load_table_in_disk() 


def union_table(ut):  # 合并表
    college_list = []

    for eve in using_table:
        for eve_ele in eve:
            college_list.append(eve_ele[0])

    college_list=list(set(college_list))
    dict_list=[]

    for eve_ut in ut:
        dict_list.append(dict(eve_ut))              #这个列表中有17个字典
    union_table=[]    #生成总表

    for cl in college_list:                   #cl表示某一个大学
        i=0
        row_list=[]
        row_list.append(cl)
        while(i<17):
            try:
                row_list.append(dict_list[i][cl])
            except:
                row_list.append("0")
            i=i+1
        union_table.append(row_list)
    return union_table


final_table=union_table(using_table)
aft=np.array(final_table)
data = pd.DataFrame(aft)
writer = pd.ExcelWriter('col_judge.xlsx')		# 写入Excel文件
data.to_excel(writer, 'page_1', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
writer.save()
writer.close()
