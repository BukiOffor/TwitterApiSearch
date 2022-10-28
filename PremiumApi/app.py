"""Script Takes 2 arguements, the query you want to search for and
 the name of the json file you want your search to be written on"""

import tweepy, os, json
import csv, sys
from access import requirements

#load keys into a bash environment
requirements()

if not sys.argv[2].endswith(('.txt','.json')):
    print(f'{sys.argv[2]} is not a supported file format, please use a (json or txt) file format')
    sys.exit()

api_key = os.environ["TWITTER_API_KEY"]
key_secret = os.environ["TWITTER_KEY_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
auth = tweepy.OAuthHandler(api_key, key_secret)
auth.set_access_token = (access_token, access_token_secret)

#instanciate our tweepy class
api = tweepy.API(auth, wait_on_rate_limit=True,parser=tweepy.parsers.JSONParser())
query = sys.argv[1]
tweet_results = api.search_30_day(label='SentimentAnalysis', query=query,)

#write our json in our local directory
with open(sys.argv[2] ,'a') as file:
    json.dump(tweet_results,file, indent=4, sort_keys=True)

print("******Successful*******")
