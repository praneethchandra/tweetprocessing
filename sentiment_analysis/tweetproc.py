#!/usr/bin/python

import tweepy

consumer_key = "Enio78hmpmgx3JhSggCCb8w8w"
consumer_secret = "ihZmcVPOvjxEsWrL3Zhnl6P0R61TpBNsKkp6tr9rnU4rNKaNUZ"

access_token = "1081956089271205888-GNEwX5KAU5VDB6zBU69A8byf1WYJzC"
access_token_secret = "iD9ektiIBRvvm9zD5A32LLNVndU2sqBChqwzUKWnwmq8y"


class TweetInterface:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)


    def getHomeTimeline(self, **kwargs):
        since_id = None
        max_id = None
        count = None
        page = None
        for key,val in kwargs.items():
            if "since_id" in key:
                since_id = val
            if "max_id" in key:
                max_id = val
            if "count" in key:
                count = val
            if "page" in key:
                page = val
        public_tweets = self.api.home_timeline(since_id=since_id, max_id=max_id, count=count, page=page)
        for index,tweet in enumerate(public_tweets):
            print index, tweet.text

    def getStatusesLookup(self, id):
        return self.api.statuses_lookup(id)

    def getUserTimeline(self, **kwargs):
        id = None
        user_id = None
        screen_name = None
        since_id = None
        max_id = None
        count = None
        page = None
        
        for key,val in kwargs.items():
            if "id" in key:
                id = val
            if "user_id" in key:
                user_id = val
            if "screen_name" in key:
                screen_name = val
            if "since_id" in key:
                since_id = val
            if "max_id" in key:
                max_id = val
            if "count" in key:
                count = val
            if "page" in key:
                page = val

        if id is None and user_id is None and screen_name is None:
            raise Exception("id or user_id or scree_name parameters are important")

        user_tweets = self.api.user_timeline(id=id, user_id=user_id, screen_name=screen_name, 
                            since_id=since_id, max_id=max_id, count=count, page=page)
        for index,tweet in enumerate(user_tweets):
            print index,tweet.text

    def getRetweetsOfMe(self, **kwargs):
        since_id = None
        max_id = None
        count = None
        page = None
        for key,val in kwargs.items():
            if "since_id" in key:
                since_id = val
            if "max_id" in key:
                max_id = val
            if "count" in key:
                count = val
            if "page" in key:
                page = val
        re_tweets = self.api.retweets_of_me(since_id=since_id, max_id=max_id, count=count, page=page)
        for index,tweet in enumerate(re_tweets):
            print index, tweet.text        

    def getStatus(self, id):
        return self.api.get_status(id)

    def doReTweet(self, id):
        return self.api.retweet(id)

    def getReTweets(self, id):
        return self.api.retweets(id)

    def getUserInfo(self, **kwargs):
        id = None
        user_id = None
        screen_name = None

        for key,val in kwargs.items():
            if "id" in key:
                id = val
            if "user_id" in key:
                user_id = val
            if "screen_name" in key:
                screen_name = val
        
        if id is None and user_id is None and screen_name is None:
            raise Exception("id or user_id or scree_name parameters are important")

        return self.api.get_user(id=id, user_id=user_id, screen_name=screen_name)

    def getFollowers(self, **kwargs):
            id = None
            user_id = None
            screen_name = None

            for key,val in kwargs.items():
                if "id" in key:
                    id = val
                if "user_id" in key:
                    user_id = val
                if "screen_name" in key:
                    screen_name = val
            
            if id is None and user_id is None and screen_name is None:
                raise Exception("id or user_id or scree_name parameters are important")

            return self.api.followers(id=id, user_id=user_id, screen_name=screen_name)

    def searchUsers(self, query):
        return self.api.search_users(q=query)

    def search(self, query):
        tweets = self.api.search(q=query)
        for index, tweet in enumerate(tweets):
            print index, tweet.text

    
def main():
    tweetInterface = TweetInterface(consumer_key=consumer_key, consumer_secret=consumer_secret,
                            access_token=access_token, access_token_secret=access_token_secret)
    # tweetInterface.getHomeTimeline(count=5)
    # tweetInterface.getUserTimeline(user_id="SenKamalaHarris")
    tweetInterface.search("#google")

if __name__ == '__main__':
    main()


                



