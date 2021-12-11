import numpy as np
import pandas as pd
import spacy
import nltk
from textblob import TextBlob

data = pd.read_csv('covid19_tweets.csv')
data.head()

tweets = np.array(data['text'])[:100]
#print(tweets)

punctuation = '!"#$%&\'()*+,-./:;<=>?[\\]^_`{|}~'

# get rid of punctuation
all_tweets = 'separator'.join(tweets)
all_tweets = all_tweets.lower()
all_text = ''.join([c for c in all_tweets if c not in punctuation])

# split by new lines and spaces
tweets_split = all_text.split('separator')
all_text = ' '.join(tweets_split)

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

#print(new_tweets)  

tweet_sentences = []
for tweet in new_tweets:
    sentence = " ".join(tweet)
    tweet_sentences.append(sentence)

#print(tweet_sentences)    



sentiment_objects = [ ]
for tweet in tweet_sentences:
    sentiment_objects.append(TextBlob(tweet))


#polarity_tweets = []
#polarity_tweet = []
category_tweet = []
category_tweets = []

#for i in range(len(tweet_sentences)):
    #polarity_tweet = [sentiment_objects[i].polarity, sentiment_objects[i]]
    #polarity_tweets.append(polarity_tweet)

for i in range(len(tweet_sentences)):
    if sentiment_objects[i].polarity > 0 :
        category_tweet = ['positive', tweet_sentences[i]]

    elif sentiment_objects[i].polarity < 0 :
        category_tweet = ['negative', tweet_sentences[i]]    

    else :
        category_tweet = ['neutral', tweet_sentences[i]]    

    category_tweets.append(category_tweet)

print(category_tweets)

