import csv
import os
import sys

#get current working directory   
path = os.getcwd()

#list files in the path
dir = os.listdir(path)
json_files = []
new_json = []

def main():
    read_oldfiles()
    get_newfiles()
    write_readfile()

#Get the old files 
def read_oldfiles():
    with open('files.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            for line in row:
               json_files.append(line)
    return json_files
#Check if there are new files in dir and returns a list 
def get_newfiles():
    i = 0
    for filename in dir:
        if filename.endswith('.json'):
            if filename not in json_files:
                new_json.append(filename)
                i += 1
    return new_json
#Appends any new file that has just been read to files.csv 
def write_readfile():
    with open('files.csv','a') as file:
        for i in new_json:
            print(f'****writing {i} to files.csv****', '\n')
            file.write(f'{i},') 

if __name__ == "__main__":
    main()