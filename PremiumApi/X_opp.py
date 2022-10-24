import tweepy
import os
import json
import csv

#load keys into a bash environment

api_key = os.environ["TWITTER_API_KEY"]
key_secret = os.environ["TWITTER_KEY_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(api_key, key_secret)
auth.set_access_token = (access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


tweet_results = api.search_30_day(label='SentimentAnalysis', query='Peter Obi', fromDate="202210100000", toDate="202210110000")
for i in range(-1,100):
    text = json.dumps(tweet_results[i]._json, indent=4, sort_keys=True)
    with open('tweets.json' ,'a') as file:
        writer = csv.DictWriter(file, fieldnames=['Data'])
        writer.writerow({"Data": text})

print("******Successful*******")
