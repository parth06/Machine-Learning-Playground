#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 05:06:20 2017

@author: parth
"""

import tweepy
from textblob import TextBlob 

consumer_key = 'RuZcRzuAcVqJn0rYa0whk9qKF'
consumer_secret = '1Zyw03zgogimAJ4xoxeuunNgnM56OVOYdYgZYZ5MaJmvI2c15E'

access_token = '886359977685909505-le0aotMkJlxOYIH0aQG5ibNpFRwMdVf'
access_token_secret = 'qwgfLVe9rWuClt6NJaFRorUVFwQzs5JUUVyVRajwmGX5D'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search(q='trmup',count=1000)
i=0
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    sentiment = analysis.sentiment.polarity
    if sentiment >= 0:
        polarity = 'Positive'
        i=i+1
    else:
        polarity = 'Negative'
    print(tweet.text, polarity)
    print("\n\n")
print ("Postive Tweets : "+ str(i))