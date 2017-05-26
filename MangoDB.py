#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pymongo
import requests
from bs4 import BeautifulSoup


client = pymongo.MongoClient('localhost', 27017)


xiaozhu = client['xiaozhu']


fangzi = xiaozhu['fangzi']


def insert_fangzi_info(url):

    wb_data = requests.get(url)


    soup = BeautifulSoup(wb_data.text, 'lxml')


    titles = soup.select('span.result_title')
    prices = soup.select('span.result_price > i')


    for title, price in zip(titles, prices):

        info = {
            'title': title.get_text(),
            'price': int(price.get_text())
        }
        fangzi.insert_one(info)


def find_fangzi():

    for info in fangzi.find():

        if info['price'] >= 500:
            print(info)


urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1, 4)]


for single_url in urls:
    # 把得到的列表页面链接，传给函数，这个函数提取房子的标题和价格
    insert_fangzi_info(single_url)
