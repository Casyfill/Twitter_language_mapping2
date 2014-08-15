#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')  

import multiprocessing

from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
import time, json, sys

import sys
sys.path.append("/root/tweetLang/code/misc")
# sys.path.append("/Users/casy/Dropbox (RN&IA'N)/Projects/Kats/Afisha/2014_06_06_Twitter2014/dropplet/misc/")
import decision, langDetect, SaveToDB, parseStamp, passes

# доступ к API
from passes import Opt_stream, Moscow_stream, Spb_stream, Dubai_stream

def scrapeGeoStream(parameters_dict):
    	
    location = parameters_dict['location']
    ckey, csecret = parameters_dict['ckey'], parameters_dict['csecret']
    atoken, asecret = parameters_dict['atoken'], parameters_dict['asecret']
    locationName = parameters_dict['name']

    class listener(StreamListener):

        def on_data(self, data):
            # print data
            temp = json.loads(data)
            if temp['coordinates']!=None:
                coord = temp['coordinates']['coordinates']
                t = langDetect.formBaseTweet(temp['text'].encode('utf-8').replace('\n',''))
                if temp['user']['lang'].encode('utf-8')==None: print ' user is None'
                d, flag = decision.decision(temp['user']['lang'].encode('utf-8'), t['text'])
                if d:
                    t['langAlert']=flag
                    t['author']=temp['user']['name'].encode('utf-8') + ' aka ' + temp['user']['screen_name'].encode('utf-8')
                    t['created_at']=temp['created_at']
                    t['userlang']= temp['user']['lang'].encode('utf-8')
                    # print temp['coordinates']['coordinates']
                    t['lon']= temp['coordinates']['coordinates'][0]
                    t['lat']= temp['coordinates']['coordinates'][1]
                    
                    print locationName , '|', t['userlang'].decode('utf-8','ignore'), '|', t['detectedLang'].decode('utf-8','ignore'), '|', t['langAlert'] , '|', t['text'].decode('utf-8')
                    # print '|'.join([str(x).decode('utf-8') for x in [locationName, t['userlang'], t['detectedLang'], t['langAlert'], t['text']]])
                    SaveToDB.SaveToDB(t, locationName )
            return True

        def on_error(self, status):
            print status

    print locationName,' started!'
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    while True:
        try:
            twitterStream.filter(locations=location)
        except Exception, e: 
            print e
            time.sleep(300)

scrapeGeoStream(Moscow_stream)
# scrapeGeoStream(Spb_stream)

# locs = [Moscow_stream]
# for loc in locs:
#     scrape_process= multiprocessing.Process(target = scrapeGeoStream, args=(loc,))
#     scrape_process.start()
    
    
