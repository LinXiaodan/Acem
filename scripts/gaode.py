#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-9-18
# Author: LXD


if __name__ == '__main__':

    output = open('../tmp/gaode/result_list', 'w+')

    with open('../tmp/gaode/city_list') as f:
        city_list = f.readlines()

    with open('../tmp/gaode/keyword_list') as f:
        keyword_list = f.readlines()

    for cityWithProvince in city_list:
        province, city = cityWithProvince.strip().split('\t')

        for keyword in keyword_list:
            output.write(','.join([province, city, keyword.strip()]))
            output.write('\n')

    output.close()