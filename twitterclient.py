import tweepy
import os
import settings

twitter_auth_keys = {
    "consumer_key"        : os.getenv("TWITTER_API_KEY"),
    "consumer_secret"     : os.getenv("TWITTER_API_SECRET"),
    "access_token"        : os.getenv("TWITTER_ACCESS_TOKEN"),
    "access_token_secret" : os.getenv("TWITTER_ACCESS_SECRET")
}

auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
        )
auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
        )

api = tweepy.API(auth)

def postTweet(tweet):
    api.update_status(status=tweet)
