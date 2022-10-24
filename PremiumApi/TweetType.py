def main():
	determine_tweet_type()

def determine_tweet_type(tweet):
   #check for reply indicator first
	if tweet['in_reply_to_status_id'] is not None:
		tweet_type = "Reply Tweet"
	# Check boolean quote status field but make sure it's not a Retweet (of a Quote Tweet)	
	elif tweet['is_quote_status'] is True and not tweet['text'].startswith('RT'):
		tweet_type = "Quoted Tweet"
	# Check both indicators of a Retweet
	elif tweet["text"].startswith("RT") and tweet.get("retweeted_status") is not None:
		tweet_type = 'Retweet'
	else:
		tweet_type = "Original Tweet"
	return tweet_type 

if __name__ == "__main__":
    main()