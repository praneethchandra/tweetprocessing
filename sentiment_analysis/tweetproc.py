#!/usr/bin/python

import tweepy

consumer_key = "Enio78hmpmgx3JhSggCCb8w8w"
consumer_secret = "ihZmcVPOvjxEsWrL3Zhnl6P0R61TpBNsKkp6tr9rnU4rNKaNUZ"

access_token = "1081956089271205888-GNEwX5KAU5VDB6zBU69A8byf1WYJzC"
access_token_secret = "iD9ektiIBRvvm9zD5A32LLNVndU2sqBChqwzUKWnwmq8y"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print tweet.text

