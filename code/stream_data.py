import tweepy
from tweepy import OAuthHandler
import json

import re

## you need to fill these info:
consumer_key = '******'
consumer_secret = '******'
access_token = '******'
access_secret = '******'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = load_api()

from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('trump.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print(&quot;Error on_data: %s&quot; % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#trump'])
