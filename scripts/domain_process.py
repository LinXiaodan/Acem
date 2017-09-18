#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-30
# Author: LXD
# 输入url，输出爬ICP的域名到文件中

from libs import domain
import csv


def main1():
    output = open('../tmp/ALY_C&P_07/result2', 'w+')

    with open('../tmp/ALY_C&P_07/kaifashanwangzhan') as f:
        lines = f.readlines()
        for line in lines:
            top_domain = domain.get_top_domain_from_domain(line.strip())
            if top_domain:
                output.write(top_domain)
                output.write('\n')

    output.close()


def main2():
    writer = csv.writer(file('../tmp/ALY_C&P_07/result_add.csv', 'wb'))
    with open('../tmp/ALY_C&P_07/kaifashanwangzhan') as f:
        lines = f.readlines()
        for line in lines:
            top_domain = domain.get_top_domain_from_domain(line.strip())
            line = line.strip()
            if top_domain:
                writer.writerow([line, top_domain])
            else:
                writer.writerow([line, ''])


def main3():
    domain_set = set()
    with open('../tmp/ALY_C&P_07/kaifashanwangzhan') as f:
        lines = f.readlines()
        for line in lines:
            top_domain = domain.get_top_domain_from_domain(line.strip())
            if top_domain:
                domain_set.add(top_domain)

    print len(domain_set)


# def main4():
    # output =


if __name__ == '__main__':
    # main2()
    main3()