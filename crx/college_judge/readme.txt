'''
  主要思路：先把每个专业排名对应的学校联系起来，构成一个字典数据结构，再把这些
  分专业的数据结构拿出来，进行去重，拼接处理，整理成为一个二维列表，再对excel进行写入


	结果在col_judge里面，代码见index_ana
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