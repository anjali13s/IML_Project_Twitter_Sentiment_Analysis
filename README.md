# Twitter Data Sentiment Analysis

There are 2 code files in our project - one for the sentiment analysis of tweets containing reviews about US airlines and another for dataset containing tweets surrounding Ashoka University


## Sentiment Analysis for Ashoka Tweets
Package dependencies for the code are tweepy, pandas, numpy and scikit-learn. 
The file titled ashoka_tweets contains the code for this.
The code for python code contains the keys required for extracting tweets have been added to the code file. Running the file would give us the tweets, the cleaned dataset, the array with the tweets and it's polarity. Then we get the model score after Multinomial Naive Bayes is done on the data frame.

## Sentiment Analysis for Airline Tweets
Package dependencies for the code are numpy, pandas, sklearn, re, nltk, keras, and tensorflow. 
The file titled SentimentAnalysis contains the code for this. It accesses the csv file named AirlineTweets.csv to get the tweets. This data is first pre-processed and then, sentiment analysis is performed using Naive Bayes and RNN-LSTM models.
