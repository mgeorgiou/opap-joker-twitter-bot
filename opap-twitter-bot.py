import tweepy
import requests, json
import opapclient
import twitterclient

def main():
    results = opapclient.get_opap_last_draw()
    print(results)

    twitterclient.postTweet(results)

if __name__ == "__main__":
    main()
