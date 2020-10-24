# coding: utf-8

import sys
from urllib import parse


def campaign_name(url):
    """Получение названия кампании из ссылки внутри строки row"""

    parsed = parse.urlsplit(url)
    params_dict = parse.parse_qs(parsed.query)

    return params_dict['re_clid'][0]


for line in sys.stdin:
	host, url = line.strip().split('\t')
	print(campaign_name(url))
