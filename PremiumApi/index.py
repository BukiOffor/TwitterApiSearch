import csv
import json
from TweetType import determine_tweet_type

tweets = []
mydict = {}
#load the json file to be cleaned 
with open('01-10.json') as file:
    data = json.load(file)

index = -1
for results in data['results']:
    index += 1
    if determine_tweet_type(data['results'][index]) == 'Retweet':
        if 'extended_tweet' in data['results'][index]['retweeted_status']:
            full_text =  data['results'][index]['retweeted_status']['extended_tweet']['full_text']
        else:
            full_text = data['results'][index]['retweeted_status']['text']
        

    elif determine_tweet_type(data['results'][index]) == 'Quoted Tweet':
        if 'extended_tweet' in data['results'][index]['quoted_status']:
            full_text = data['results'][index]['quoted_status']['extended_tweet']['full_text']
        else:
            full_text = data['results'][index]['quoted_status']['text']

    else:
        if 'extended_tweet' in data['results'][index]:
            full_text = data['results'][index]['extended_tweet']['full_text']
        else:
            full_text = data['results'][index]['text']


    mydict = { "tweet_id": data['results'][index]["id_str"],
                       "date":data['results'][index]["created_at"],
                       "full_text": full_text,
                       "tweet_type": determine_tweet_type(data['results'][index]),
                        "reply_count": data['results'][index]["reply_count"], #Number of times Tweet has been replied to
                       "quote_count": data['results'][index]["quote_count"], # Number of times Tweet has been quoted
                       "likes_count": data['results'][index]["favorite_count"], #Number of times Tweet has been liked 
                       "retweet_counts": data['results'][index]["retweet_count"], #Number of times this Tweet has been retweeted
                       "location": data['results'][index]['user']['location'],
                       "name": data['results'][index]['user']['name'],
                       'username': data['results'][index]['user']['screen_name'],
                       "hyperlink": "https://twitter.com/twitter/status/" + data['results'][index]["id_str"]
              }
    tweets.append(mydict)

with open('compiled_tweets.txt', 'a') as file:
    writer = csv.DictWriter(file, fieldnames=['Data',])
    for info in tweets:
        writer.writerow({'Data': info}) 

    
print("*******Successful********")

