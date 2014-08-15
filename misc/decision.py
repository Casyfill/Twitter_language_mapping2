#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
sys.path.append("/root/tweetLang/code/misc")
# sys.path.append("/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/2014_06_06_Twitter2014/dropplet/misc/")
from langDetect import langObg



# Логика, сохранять ли объект. возвращает 
def decision (interface, text):

	langdetect, langdetectRatio = langObg(text)
	
	stopList= ["I'm at"]
	# если интерфейс русский
	for word in stopList:
		if word in text:
			return False, False

	if interface == 'ru':
		# апд - тогда нет
		return False,False
		# но детект говорит обратное и уверенность > 0.8
		# if langdetect not in ['ru']:
		# 	if langdetectRatio>=0.95:
		# 		# пускаю с флагом
		# 		return True, True
		# else:
		# 	return False, False
	else:
		# если интерфейс не русский
		# если детект определяет как русский, 
		# но уверенность меньше 0.6,
		# пока пускаю с флагом
		if langdetect == 'ru':
			if langdetectRatio<=0.4:
				return True, True
			else:
				# если больше, не пускаю
				return False, False
		# если детектор тоже иностранный, пускаю без флага
		else:
			if interface == langdetect:
				return True, False
			else:
				return True, True
	
	
		