#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# import sys  
# reload(sys)  
# sys.setdefaultencoding('utf-8')  

db = ''
user = ''
password = ''

import peewee
from peewee import *

def SaveToDB(TweetDict, locationName):
	db = MySQLDatabase(db, user=user,passwd=password) #DIGITALOCEAN
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
		name = peewee.CharField()

		class Meta:
			database = db


	# Если нужно, создаем базу
	if u'tweet2' not in db.get_tables():
		Tweet2.create_table()

	tweet = Tweet2(author=TweetDict['author'].decode('utf-8'), #автор твита
				  text=str(TweetDict['text']).decode('utf-8', 'ignore'),  #текст твита
				  hashtags = TweetDict['hashtags'].decode('utf-8'), # хэштеги
				  links = TweetDict['links'].decode('utf-8'), # ссылки
				  mentions = TweetDict['mentions'].decode('utf-8'), # имена
				  created_at = TweetDict['created_at'].decode('utf-8'), # время поста
				  lon = TweetDict['lon'], #широта
				  lat = TweetDict['lat'], #долгота
				  detectedLang = TweetDict['detectedLang'].decode('utf-8'), #язык
				  langAlert = TweetDict['langAlert'], #флажок
				  lRatio=TweetDict['detectedLangRatio'],
				  userLang = TweetDict['userlang'].decode('utf-8'),
				  name = locationName ) # 
	tweet.save()
	# print 'another one saved!'


# for tweet in Tweet.filter(author="me"):
#     print tweet.text
def dropTable():
	db = MySQLDatabase('twitterLang2', user='casy',passwd='26011986')

	class Tweet(peewee.Model):
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
		name = peewee.CharField()

		class Meta:
			database = db
	Tweet.drop_table()
	print db.get_tables()

def checkTable():
	db = MySQLDatabase('twitterLang2', user='casy',passwd='26011986')
	print db.get_tables()

# dropTable()
# checkTable()