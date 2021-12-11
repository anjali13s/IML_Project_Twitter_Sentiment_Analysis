import numpy as np
import pandas as pd
import spacy

data = pd.read_csv('covid19_tweets.csv')
data.head()

tweets = np.array(data['text'])[:1000]
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

print(new_tweets)  
'''
nlp = spacy.load("en_core_web_sm")
doc = []
for tweet in new_tweets:
    for text in tweet:
            word = nlp(text)
    doc.append(word)
    token_list = [token for token in doc]

#print(token_list)

filtered_tokens = []
for word in doc:
    filtered = [token for token in word if not token.is_stop]
    filtered_tokens.append(filtered)

print(filtered_tokens)    

#lemmas = [ f"Token: {token}, lemma: {token.lemma_}" for token in filtered_tokens]
#print(lemmas)
'''