#!/usr/bin/env python
#-*- coding: utf-8 -*-

import peewee, csv
from peewee import *

path = "/root/tweetLang/data/dump.csv"


def serialiseMysql(Obj):
	return[Obj.author.encode('utf-8').replace('\n',''),
			Obj.text.encode('utf-8').replace('\n',''),
			Obj.hashtags.encode('utf-8').replace('\n',''),
			Obj.links.encode('utf-8').replace('\n',''),
			Obj.mentions.encode('utf-8').replace('\n',''),
			Obj.created_at.encode('utf-8'),
			str(Obj.lon),
			str(Obj.lat),
			str(Obj.lRatio),
			Obj.detectedLang.encode('utf-8'),
			str(Obj.langAlert),
			Obj.userLang.encode('utf-8')]


def dumpToCSV(path):

	db = MySQLDatabase('tweetLang2', user='twitterHenerator',passwd='26011986')
	db.connect()

	class Tweet2(peewee.Model):
			author = peewee.CharField()
			text = peewee.TextField()
			hashtags = peewee.TextField()
			links = peewee.TextField()
			mentions = peewee.TextField()
			created_at = peewee.TextField()
			lon = peewee.FloatField()
			lat = peewee.FloatField()
			lRatio = peewee.FloatField()
			detectedLang = peewee.CharField()
			langAlert = peewee.BooleanField()
			userLang = peewee.CharField()

			class Meta:
				database = db


	query = Tweet2.select().execute()
	with open(path, 'w') as csvfile:
	    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	    
	    # write headers
	    writer.writerow(['author','text', 'hashtags','links','mentions','created_at','lon','lat','lRatio','detectedLang','langAlert','userLang'])
	    
	    cnt = 0
	    lStats = {}
	    for q in query.iterator():
	    	x = serialiseMysql(q)
	    	writer.writerow(x)
	    	cnt+=1
	    	if x[-3] in lStats.keys():
	    		lStats[x[-3]]+=1
	    	else:
	    		lStats[x[-3]]=1

	    print 'records: ', cnt
	    # for key in lStats:
	    # 	print key, ': ', lStats[key]



dumpToCSV(path)