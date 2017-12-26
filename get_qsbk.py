#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import os
def get_information():
    num = int(raw_input("Please Input Page Number:"))
    while num > 0:
        s = requests.get('http://www.qiushibaike.com/hot/page/'+str(num))
        soup = BeautifulSoup(s.text, "lxml")
        for i in soup.select('div .content'):
            print i.get_text().encode('utf-8','ignore')
            t = raw_input()
        t = raw_input("Jokes in current page is over please input enter button to next page!")
        num = num + 1
    raw_input("Page number less than one")

if __name__ == '__main__':
    get_information()

