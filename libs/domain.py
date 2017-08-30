#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on 17-8-30
# Author: LXD

import re


Domain = (
    'ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'az', 'ba', 'bb',
    'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bm', 'bn', 'bo', 'br', 'bs', 'bt', 'bv', 'bw', 'by', 'bz', 'ca', 'cc',
    'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cx', 'cy', 'cz', 'de', 'dj', 'dk',
    'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'er', 'es', 'et', 'eu', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gd', 'ge',
    'gf', 'gg', 'gh', 'gi', 'gl', 'gm', 'gn', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gw', 'gy', 'hk', 'hm', 'hn', 'hr',
    'ht', 'hu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'ir', 'is', 'it', 'je', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh',
    'ki', 'km', 'kn', 'kr', 'kw', 'ky', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma',
    'mc', 'md', 'me', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mo', 'mp', 'mq', 'mr', 'ms', 'mt', 'mu', 'mv', 'mw', 'mx',
    'my', 'mz', 'na', 'nc', 'ne', 'nf', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nu', 'nz', 'om', 'pa', 'pe', 'pf', 'pg',
    'ph', 'pk', 'pl', 'pm', 'pn', 'pr', 'ps', 'pt', 'pw', 'py', 'qa', 're', 'ro', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd',
    'se', 'sg', 'sh', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'st', 'sv', 'sy', 'sz', 'tc', 'td', 'tf', 'tg', 'th',
    'tj', 'tk', 'tl', 'tm', 'tn', 'to', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'uk', 'us', 'uy', 'uz', 'va', 'vc',
    've', 'vg', 'vi', 'vn', 'vu', 'wf', 'ws', 'ye', 'yt', 'yu', 'za', 'zm', 'zw', 'com', 'net', 'org', 'gov', 'mil',
    'edu', 'biz', 'info', 'pro', 'name', 'coop', 'travel', 'xxx', 'idv', 'aero', 'museum', 'mobi', 'asia', 'tel', 'int',
    'post', 'jobs', 'cat', 'top', 'arpa', 'xin', 'shop', 'ltd', 'win', 'club', 'wang', 'top', 'vip', 'xyz', 'store',
    'pub', 'cc', 'site', 'ren', 'lol', 'bid', 'mom', 'online', 'tech', 'biz', 'red', 'website', 'space', 'link', 'news',
    'date', 'loan', 'mobi', 'press', 'video', 'market', 'live', 'studio', 'help', 'info', 'click', 'pics', 'photo',
    'science', 'party', 'rocks', 'brand', 'gift', 'wiki', 'design', 'software', 'social', 'lawyer', 'engineer', 'name',
    'asia', '我爱你', 'work', '中国', '公司', '网络', '集团'
)


def get_top_domain_from_domain(url):
    """
    :param url: domain
    :return: top domain
    """
    docs = re.split('/|\?', url.lower())
    for doc in docs:
        if not (doc == 'http:' or doc == 'https:' or doc == ''):
            parts = doc.split('.')
            if len(parts) == 2:
                return doc
            elif len(parts) > 2:
                for index in range(len(parts)-1, -1, -1):
                    if not parts[index] in Domain:
                        if not parts[index] == 'www':
                            return '.'.join(parts[index:])
                        else:
                            return doc
            # 未知域名情况
            else:
                return url


if __name__ == '__main__':
    # temp()
    print get_top_domain_from_domain('www.cocos2d-x.org')
    print get_top_domain_from_domain('http://blog.sina.com.cn/s/blog_6afaefbe0100xy59.html')
    print get_top_domain_from_domain('weibo.com')
    print get_top_domain_from_domain('www.yn.10086.cn')
    print get_top_domain_from_domain('ps.sysucc.org.cn')
    print get_top_domain_from_domain('https://jz.zulong.com')