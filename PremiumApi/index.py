'''This scripts imports functions from parse.py that checks for json files in the directory,
   Checks if the files have been extracted, if any json file in the folder has not been extracted
   it extracts it and writes the name of the extracted file in files.csv,  
'''
import csv
import json
from TweetType import determine_tweet_type
from parse import read_oldfiles,write_readfile,get_newfiles

tweets = []
mydict = {}

#checks the old file in the directory 
read_oldfiles()
print('****old files read succesfully****', '\n')
print('-----loading unread files-----','\n')
#checks if any new file is in the directory and returns it as a a list
files = get_newfiles()
if len(files) < 1:
    print("-----no new Files-----", '\n')
    print('!!please move json files to current working folder!!', '\n')
    sys.exit()


print(f"{len(files)} files to be cleaned", '\n')
#load the json file to be cleaned 
for i in files:
    print(f'******cleaning {i}*******', '\n')
    with open(i) as file:
        data = json.load(file)
#Get the Full Text of a tweet from the Json file
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

# Select other informations you want from the json file 
    mydict = { "tweet_id": data['results'][index]["id_str"],
                       "datae":data['results'][index]["created_at"],
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
  # append selected information into a dictionary            
    tweets.append(mydict)

#Write your retrived data in a txt file in the directory
with open('compiled_tweets.txt', 'a') as file:
    writer = csv.DictWriter(file, fieldnames=['data',])
    for info in tweets:
        writer.writerow({'data': info}) 

#write file that was just read in file.csv so that read_oldfiles() remebers that it has been read
write_readfile()

print("****new files written*****", '\n')
    
print("*******Task Successful********")

