import pymongo
import config
import os



# 1. Connect to a collection of a given database
# 2. Read in all data as adjacency list
# 3. Out adjancency list in the form accepted in NetworkGrapher p5.js program I wrote

def connect():
    client = config.connect
    db = client.wiki
    return db.pages

# Read in csv -> filter out unnecessary data
def read_in_collection():
    collection = connect()
    list_collection = list(collection.find())
    print(list_collection[0])
    # num = 0
    # for ele in collection.find({}):
    #     num += 1
    #     print(ele)
        
    # print(f"Number documents: {num}")

def write_to_file():
    print("Writing database to file.")
    cmd = 'mongoexport --uri mongodb+srv://brenden_wds:Ky4QAoSP5yhSSU5W@cluster0.vvn5s.mongodb.net/wiki --collection pages --type=csv --out output.csv --fields page_name,links'
    os.system(cmd)
    print("Done writing to file.")


def main():
    write_to_file()
    # read_in_collection()
if __name__ == '__main__':
    main()
    