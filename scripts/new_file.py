#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-15
# Author: LXD
# 输出指定文件

import os
import time


def file_type_1(filepath, a, b):
    """
    将从a到b按行输出到指定文件filepath中
    :param filepath: 
    :param a: 
    :param b: 
    :return: 
    """
    path = os.path.dirname(filepath)
    if not os.path.exists(path):
        os.makedirs(path)

    with open(filepath, 'w+') as output:
        for i in range(a, b+1):
            output.write(str(i)+'\n')

if __name__ == '__main__':
    file_type_1('../tmp/file_tmp/{}'.format(int(time.time()*1000)), 1, 1000000)