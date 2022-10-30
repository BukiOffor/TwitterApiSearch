import sqlite3
import json
import sys

con = sqlite3.connect('extracts.db')
cur = con.cursor()

def main():
    createDb()
    sys.exit()
    insert()

def createDb():
    cur.execute('''
            CREATE TABLE IF NOT EXISTS 
            tweets(name,username,full_text,location,date,tweet_id,tweet_type,hyperlink)
            ''')
    con.commit()
        
def insert(Somefile):
    with open(Somefile)as file:
        data = json.load(file)
        for i in data:
            tweetdata = [i['name'],i['username'],i['full_text'],i['location'],i['date'],i['tweet_id'],i['tweet_type'],i['hyperlink']]
            cur.execute("INSERT INTO tweets VALUES (?,?,?,?,?,?,?,?)", tweetdata)
            con.commit()


if __name__ == "__main__":
    main()