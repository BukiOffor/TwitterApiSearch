import csv
import json
import sys

keys = [
    'date','full_text','hyperlink','likes_count',
    'location','name','username', 'tweet_id','tweet_type', 
    'quote_count','reply_count','retweet_count'
]
def main():
    requirements()
    checkpoint()
    #index into cleaned json file
    with open(sys.argv[1]) as file:
        data = json.load(file)
        for key in data:
            print(key[sys.argv[2]])

#make sure input is a recognized file format and keys in the json           
def checkpoint():
    if not sys.argv[1].endswith(('.txt','.json','.csv')):
        print(f'{sys.argv[1]} file format not supported please use a (csv, json or txt) file format')
        sys.exit()
    elif sys.argv[2] not in keys:
        print(f'***Sorry your argument cannot be found in {sys.argv[1]}')
        sys.exit()

#make sure arguements passed are enough and take care of errors
def requirements():
    if len(sys.argv) < 3:
        print('*** Sorry, your command is missing an arguement, please specify file and parameter to retrieve')
        sys.exit()
    elif len(sys.argv) > 3:
        print('****Too many Commands, please specify just file and parameter to retrieve')
        sys.exit()
    else:
        pass

if __name__ == '__main__':
    main()