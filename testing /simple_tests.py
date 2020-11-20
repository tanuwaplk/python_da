# coding: utf-8


def word_count(phrase):
	return len(phrase.split(' '))


def test_word_count():
	assert word_count('мрт менделеевская') == 2
	assert word_count('') == 0
