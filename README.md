# **Twitter API** 

This repository contains explanatory codes on how to work with twitter premium and twitter Api v02. The scripts aims to search twitter APi, return a json file, extract information from the json file and store the information in a database. This  repository focuses more on the premium Api because its more difficult to work with and has fewer resources around.

---

## **Script Structure**
```bash
python3 app.py 'query' query.json 
``` 
This script takes 2 arguments, the query you want to search for and the name of the json file you want your search to be saved as. it returns tweets within the last 30 days and a max results of 100 tweets per request.
  
    python3 index.py
 This script searches all the json file in your directory, extracts information from them and stores in a database. Also returns a txt/json file of the information. 
 
```bash
 python3 access.py file.json 'username'
 ```
This script takes 2 arguements, name of a json file and the information you want to extract from it. *The file must have been cleaned by index.py*

    python3 db.py
when run, creates a database named extracts. Contains codes that inserts information to the database.

    files.csv
Logs extracted json files. To repeat extracted filenames be sure to delete used names from files.csv. 

---

### **DOCUMENTATIONS**
[Twitter Api Documentation](https://developer.twitter.com/en/docs/twitter-api/premium/search-api/api-reference/premium-search)

[Tweepy Documentaion](https://docs.tweepy.org/en/stable/api.html#premium-search-apis)

---
**NOTE**

Be sure to export your API keys into your prefered terminal or edit the script and manually fill it in. If something goes wrong while running, the script should provide you information about possible failures. Feel free to edit the code to better your search.
