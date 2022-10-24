import tweepy
import os
import json


api_key = os.environ["TWITTER_API_KEY"]
key_secret = os.environ["TWITTER_KEY_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
b_token = os.environ["TWITTER_BEARER_TOKEN"]


client = tweepy.Client(bearer_token=b_token)

query = "Peter Obi -is:retweet"
tweets = tweepy.Paginator(client.search_recent_tweets,query=query,tweet_fields=['context_annotations','created_at',],place_fields=['full_name','country_code','country','geo'],user_fields=['location',],max_results=10).flatten(limit=2)

data = json.loads(tweets)
    