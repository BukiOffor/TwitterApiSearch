import tweepy
import os
import json
import csv
import sys

#load keys into a bash environment

api_key = os.environ["TWITTER_API_KEY"]
key_secret = os.environ["TWITTER_KEY_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(api_key, key_secret)
auth.set_access_token = (access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,parser=tweepy.parsers.JSONParser())
query = sys.argv[1]

tweet_results = api.search_30_day(label='SentimentAnalysis', query=query, fromDate="202210160000", toDate="202210170000")

with open('tweets.json' ,'a') as file:
    json.dump(tweet_results,file, indent=4, sort_keys=True)

print("******Successful*******")
