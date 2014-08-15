#!/usr/bin/env python
#-*- coding: utf-8 -*-

import langid
import re


# распознавание языка
def langObg(txt):
	# распознавание языка
	lang, lRatio = langid.classify(txt)
	return lang, lRatio

def chechCyrillic(txt):
	# проверка, есть ли кириллические буквы
	p = re.compile('.*[а-я,А-Я].*')


# ссылки, хэштеги и имена из текста, очищенный текст
def formBaseTweet(txt):

	def filterHastags(txt):
		if '#' not in txt:
			return txt, []
			# print 'no hashtags'
		else:
			p = re.compile('#\w*')
			hashtags = p.findall(txt)
			for hashtag in hashtags:
				txt = txt.replace(hashtag, '')
			ws = re.compile('\s\s+')
			txt = ws.sub(' ',txt).strip()
			return txt, hashtags

	def filterLinks(txt):
		p = re.compile('http:[\w/.]*')
		links = hashtags = p.findall(txt)
		for link in links:
			txt = txt.replace(link, '')
		ws = re.compile('\s\s+')
		txt = ws.sub(' ',txt).strip()
		return txt, links

	def filterPeople(txt):
		if '@' not in txt:
			return txt, []
			# print 'no hashtags'
		else:
			p = re.compile('@\w*:?')
			names = p.findall(txt)
			for name in names:
				txt = txt.replace(name, '')
			names = [name.replace('RT ','').replace(':','') for name in names]

			ws = re.compile('\s\s+')
			txt = ws.sub(' ',txt).strip()
			return txt, names

	def filterEMOJI(txt):
		emoji = [':-)',':)',':-(',':(',':-P','B)','B-)',".-)",'))']
		for e in emoji:
			if e in txt:
				txt=txt.replace(e,'')
		return txt


	t, h = filterHastags(txt)
	t, l = filterLinks(t)
	t,n = filterPeople(t)
	t = filterEMOJI(t)

	tweet = {'text':t, 'mentions':'|'.join(n), 'links':'|'.join(l), 'hashtags':'|'.join(h)}
	tweet['detectedLang'], tweet['detectedLangRatio'] = langObg(t)
	return tweet
