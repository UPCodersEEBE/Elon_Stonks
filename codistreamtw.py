# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:31:32 2021

@author: leona
"""

import tweepy

class TweetsListener(tweepy.StreamListener):
    def on_connect(self):
        print("Working")
    
    def on_status(self,status):  #aqui es pot guardar una base de dades de piulades actuals
        print(status.text)
    def on_error(self,status_code):
        print("Error",status_code)
        
    
    

consumer_key = "y9iuklm5x6J00j1jST7xMvELc"
consumer_secret = "p3OsGkS8vPHrL3VGPfJS1yPUiTwbrxt7eyPH9uGvpLfcHRTX6b"
access_token = "2307220706-lHanCvNdgV9v7irKnrKwmNpeRsczsoYOjjhEMvA"
access_token_secret = "PoRfn9EnqiqHTx6D9HozWc4AdwYLAYB0QKGrxRlsCDS8S"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

stream = TweetsListener()
streamingApi= tweepy.Stream(auth=api.auth, listener=stream)
#follow ens diu a qui esta escoltant l'stream tweet
#track ens diu una llista del que passa
streamingApi.filter(
    follow=["2307220706"]
    
    
    )

