#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-7-24
# Author: LXD
# 文件操作的一系列方法的函数封装

import os
import time


def read_file_to_list(filepath):
    """
    按照行读取文件中每一行保存到list中（将换行符去掉）
    :param filepath: 文件路径
    :return: list
    """
    new_list = []
    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            new_list.append(line.strip('\n'))
    return new_list


def write_list_to_file(filepath, save_list):
    """
    将list中的每一项按照行存到文件中
    :param filepath: 文件路径+文件名
    :param save_list: 要保存的list
    :return: None
    """
    # 创建没有的路径
    path = os.path.dirname(filepath)
    if not os.path.exists(path):
        os.makedirs(path)

    with open(filepath, 'w+') as output:
        for i in save_list:
            if isinstance(i, unicode):
                output.write(i.encode('utf8'))
            else:
                output.write(i)
            output.write('\n')