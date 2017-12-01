# Simple Twitter Sentiment Analysis by lukaspman
import tweepy
from textblob import TextBlob

# authentication keys for twitter
consumer_key = '-'
consumer_secret = '-'

access_token = '-'
access_token_secret = '-'

# authenticate to twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def getSentiment(topic):
    public_tweets = api.search('{0}'.format(topic))

    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
        print("")


print('Welcome to the simple python sentiment analysis')
print()

topic = str(input('Enter topic you want to analyse: '))

getSentiment(topic)
