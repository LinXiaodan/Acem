#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-30
# Author: LXD
# 输入url，输出爬ICP的域名到文件中

from libs import domain

output = open('../tmp/ALY_C&P_07/result', 'w+')

with open('../tmp/ALY_C&P_07/kaifashanwangzhan') as f:
    lines = f.readlines()
    for line in lines:
        top_domain = domain.get_top_domain_from_domain(line.strip())
        if top_domain:
            output.write(top_domain)
            output.write('\n')

output.close()