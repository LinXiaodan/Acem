#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-7-24
# Author: LXD
# Project: GaoDe_0001
# 提取公司信息中公司名与地址，按照address1|address2|...#split#name1|name2|...的格式存储

import json
import time
from libs import file


def main(filename, save_filename):
    address = []
    name = []
    max_num = 10
    num = 0
    error_num = 0
    output = open(save_filename, 'w+')
    lines = file.read_file_to_list(filename)

    empty_num = 0
    for data in lines:
        doc = json.loads(data.decode('utf-8'))
        try:
            temp = doc['address']
            temp_address = ''
            # 一种address为dict， 一种address就是地址
            if isinstance(temp, dict) or isinstance(temp, list):
                # 一种地址在value中，一种地址在address的value中
                if 'value' in temp:
                    if isinstance(temp['value'], dict):
                        temp_address = temp['value']['value']
                    else:
                        temp_address = temp['value']
                elif 'address' in temp:
                    temp_address = temp['address']['value']
            else:
                temp_address = temp
            # 删掉地址为空的情况
            if not temp_address == '':
                address.append(temp_address)
                name.append(doc.get('name', ''))
            else:
                print 'address empty', temp
                empty_num = empty_num + 1
                continue

        except Exception as e:
            print 'decode error', doc
            error_num = error_num + 1
            continue

        num = num + 1
        if num % max_num == 0 or num == len(lines):
            str1 = '|'.join(address)
            str2 = '|'.join(name)
            str = str1 + '#split#' + str2
            # print str
            if isinstance(str, unicode):
                output.write(str.encode('utf8'))
            else:
                output.write(str)
            output.write('\n')
            address = []
            name = []
    output.close()
    print 'error_num:', error_num
    print 'empty_num', empty_num

if __name__ == '__main__':
    main('../tmp/company_info/yz-addresss.json', '../tmp/company_info/result_{}'.format(int(time.time())))