#!/usr/bin/env python
#-*- coding: utf-8 -*-
from datetime import datetime

def parseStamp(s):
	
	s = s.split(' ')[:4] + [s.split(' ')[-1]]
	s = ' '.join(s)
	# print s
	return datetime.strptime(s, "%a %b %d %H:%M:%S %Y")