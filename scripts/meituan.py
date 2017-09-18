#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-9-15
# Author: LXD

from pypinyin import lazy_pinyin


def name2pinyin(name):
    """城市名转为拼音"""
    result = ''.join(lazy_pinyin(unicode(name, 'utf8')))
    return result

if __name__ == '__main__':
    with open('../tmp/meituan/city_list') as f:
        city_list = f.readlines()

    with open('../tmp/meituan/keyword_list') as f:
        keyword_list = f.readlines()

    output = open('../tmp/meituan/result_list', 'w+')

    for item in city_list:
        province, city = item.strip().split('\t')
        pinyin = name2pinyin(city)
        for keyword in keyword_list:
            result = ','.join([province, city, pinyin.encode('utf8'), keyword.strip()])
            output.write(result)
            output.write('\n')

    output.close()