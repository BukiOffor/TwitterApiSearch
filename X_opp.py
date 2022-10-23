import tweepy
import os
import json
import csv


api_key = os.environ["TWITTER_API_KEY"]
key_secret = os.environ["TWITTER_KEY_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(api_key, key_secret)
auth.set_access_token = (access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

dict_ = {}

dict_["tweet_results"] = api.search_30_day(label='SentimentAnalysis', query='Peter Obi', fromDate="202210100000", toDate="202210110000")
#text = json.dumps(tweet_results[0]._json, indent=4, sort_keys=True)
with open("tweets.txt", 'a') as file:
   writer = csv.DictWriter(file, fieldnames=["Data",])
   for tweets in dict_["tweet_results"]:
        writer.writerow({'Data': tweets})