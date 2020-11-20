# coding: utf-8

import pytest
from useful_functions import word_count, campaign_name


class TestFunctions:
	def test_word_count(self):
		assert word_count('мрт менделеевская') == 2
		assert word_count('') == 0

@pytest.mark.parametrize(
	'test_input,expected',
	[
		('https://awesome-site.ru/?utm_source=yandex&utm_medium=cpc&utm_campaign=a825749b87&utm_content=dev_{device_type}', 'a825749b87'),
		('https://awesome-site.ru/?utm_source=yandex&utm_medium=cpc&utm_content=dev_{device_type}', ''),
	]
)
def test_campaign_name(test_input, expected):
	assert campaign_name(test_input) == expected
