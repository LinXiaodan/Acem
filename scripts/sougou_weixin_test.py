#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-7-28
# Author: LXD
# 搜狗微信公众号搜索结果名称数目不重复统计

from libs import file
import re


def main(filename):
    lines = file.read_file_to_list(filename)
    word_set = set()
    no_set = set()
    for line in lines:
        m = re.search('save result, search:(.*)$', line)
        if m:
            word = m.group(1)
            word_set.add(word)
        m2 = re.search('has no result, search:(.*)$', line)
        if m2:
            word = m2.group(1)
            no_set.add(word)
    print '总行数：', len(lines)
    print '有结果数：', len(word_set)
    print '没有结果数：', len(no_set)

if __name__ == '__main__':
    main('../tmp/sougou_weixin/temp_sougou_test1_info.log')