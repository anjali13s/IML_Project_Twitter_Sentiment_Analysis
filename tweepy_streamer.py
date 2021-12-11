import tweepy
import random
import json
import numpy as np
import pandas as pd

auth = tweepy.OAuthHandler("wvID4HbxNGrL9gEn7HtyaqY98", "CBbRMJSTQvNRJHASjvHI5Vmm0bvoku8nhIbMyqJP0XfQQilQTZ")
consumer_key = "t6nkbhDcmFMc7aHFLi70TX0k7"
consumer_secret = "E2fHiqfgx2BAba2tbwKOSnvvIsPZatHMgqujkbEgCfTgvcjc7d"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAHo%2BWwEAAAAAdMKyzHW7qRYwmwBmSfAXUglk6%2Bw%3DVH9D2JBGD2QfVqxOIk5yuPyV3JgRb3Xe5FKwl7B0PRQi5KqpLI"
access_token = "1469208266198732803-REOnVL3cmm7hBcvfPTAoqJQh4moyou"
access_token_secret = "zpEe1k4HLWLCY8EIY6pDltde2niMLPfjgt3NEq7TMOLMQ"


def getClient():
    client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAHo%2BWwEAAAAAdMKyzHW7qRYwmwBmSfAXUglk6%2Bw%3DVH9D2JBGD2QfVqxOIk5yuPyV3JgRb3Xe5FKwl7B0PRQi5KqpLI", 
                           consumer_key="t6nkbhDcmFMc7aHFLi70TX0k7", 
                           consumer_secret= "E2fHiqfgx2BAba2tbwKOSnvvIsPZatHMgqujkbEgCfTgvcjc7d",
                           access_token="1469208266198732803-REOnVL3cmm7hBcvfPTAoqJQh4moyou", 
                           access_token_secret="zpEe1k4HLWLCY8EIY6pDltde2niMLPfjgt3NEq7TMOLMQ")

    return client


def searchTweets(query):
    client = getClient()

    tweets = client.search_recent_tweets(query=query, max_results=100)

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

##pre-processing

punctuation = '!"#$%&\'()*+,-./:;<=>?[\\]^_`{|}~'

# get rid of punctuation
all_tweets = 'separator'.join(ashoka_tweets)
all_tweets = all_tweets.lower()
all_text = ''.join([c for c in all_tweets if c not in punctuation])

# split by new lines and spaces
tweets_split = all_text.split('separator')
all_text = ' '.join(tweets_split)

print(all_text)

# create a list of words
words = all_text.split()

# get rid of web address, twitter id, and digit
new_tweets = []
for tweet in tweets_split:
    tweet = tweet.split()
    new_text = []
    for word in tweet:
        if (word[0] != '@') & ('http' not in word) & (~word.isdigit() & ('rt' not in word)):
            new_text.append(word)
    new_tweets.append(new_text)

print(new_tweets)    