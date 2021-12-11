import tweepy
import random
import json


#consumer_key = "t6nkbhDcmFMc7aHFLi70TX0k7"
#consumer_secret = "E2fHiqfgx2BAba2tbwKOSnvvIsPZatHMgqujkbEgCfTgvcjc7d"
#BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHo%2BWwEAAAAAdMKyzHW7qRYwmwBmSfAXUglk6%2Bw%3DVH9D2JBGD2QfVqxOIk5yuPyV3JgRb3Xe5FKwl7B0PRQi5KqpLI"
#access_token = "1469208266198732803-REOnVL3cmm7hBcvfPTAoqJQh4moyou"
#access_token_secret = "zpEe1k4HLWLCY8EIY6pDltde2niMLPfjgt3NEq7TMOLMQ"

auth = tweepy.OAuthHandler(consumer_key="t6nkbhDcmFMc7aHFLi70TX0k7", consumer_secret="E2fHiqfgx2BAba2tbwKOSnvvIsPZatHMgqujkbEgCfTgvcjc7d")
auth.set_access_token(key = "1469208266198732803-REOnVL3cmm7hBcvfPTAoqJQh4moyou" , secret = "zpEe1k4HLWLCY8EIY6pDltde2niMLPfjgt3NEq7TMOLMQ")

def getAPI():
    API = tweepy.API(auth)

    return API


def searchTweets(query):
    API = getAPI()

    tweets = API.search_tweets(q =query, count=100)

    tweet_data = tweets.data
    text = []
    for tweet in tweet_data:
        text.append(tweet.text)
    
    results = []


    if not tweet_data is None and len(tweet_data) > 0:
        for tweet in tweet_data:
            obj = {}
            obj['id'] = tweet.id
            obj['text'] = tweet.text
            results.append(obj) 

    else:
        return ''

    only_text = []
    for tweet in text:
        if tweet not in only_text:
            only_text.append(tweet)


    return only_text         


ashoka_tweets = searchTweets("Ashoka university")
for x in ashoka_tweets:
    print(x)
print(len(ashoka_tweets))
