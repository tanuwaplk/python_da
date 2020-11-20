# coding: utf-8

from urllib import parse


def word_count(phrase):
	if phrase:
		return len(phrase.split(' '))
	else:
		return 0


def campaign_name(url):
    parsed = parse.urlsplit(url)
    params_dict = parse.parse_qs(parsed.query)

    if 'utm_campaign' in params_dict:
    	return params_dict['utm_campaign'][0]
    else:
    	return ''
