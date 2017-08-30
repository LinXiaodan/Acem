#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-23
# Author: LXD
# 统计搜狗微信公众号去重结果

import json
import logging
logging.basicConfig(level=logging.INFO)


def main(filepath, writepath):
    output = open(writepath, 'w+')
    with open(filepath) as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            try:
                data = json.loads(line)
                ID_set = set()
                ID = data['t:weChatID'].strip()
                name = data['t:weChatName_59798c99098f6b1a0cf5df9f'].strip()
                if ID is not '' and ID not in ID_set and name is not '':
                    count = count+1
                    ID_set.add(ID)
                    output.write(line)
                else:
                    logging.info('repeat {}'.format(line))
            except:
                logging.info(line)

    output.close()
    print 'total count:', count

if __name__ == '__main__':
    main('../tmp/sougou_weixin/wechat.json', '../tmp/sougou_weixin/wechat_result.json')