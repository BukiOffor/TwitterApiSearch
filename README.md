USAGE(PremiumAPI):

python3 app.py 'query' query.json

app.py queries the twitter api and returns a json file, the json file is saved to your local directory as the name of the file you passed. This script returns tweets in the last 30 days with a max result of 100 tweets. Edit the script to your needs, if you need more. Documentations at https://docs.tweepy.org/en/stable/api.html#premium-search-apis, https://developer.twitter.com/en/docs/twitter-api/premium/search-api/api-reference/premium-search

python3 index.py
This script searches all the json file in your directory and cleans up the original json file leaving only the necessary parameters and then prompts you for the name you want the recently cleaned json file to be saved as. This scripts returns a new_json or txt file to your local dir.

python3 access.py 'cleaned_jsonfile' username
This script takes a key as sys.argv[2] and returns all the values of the key in the given file. you can write the output in another file with a bit of bash scripting e.g.
python3 access.py 'json_file' full_text >> output.txt

files.csv
This file logs cleaned json files. if you want to repeat file names be sure to manually delete it from the file.csv log else the script will insist on no new files.

NOTE!!!
These scripts works correctly only for Twitter PremiumAPI v1 because of the json file structure. if you are using API v02, please edit the scrpits to serve your needs correctly.
