import pymongo
from pymongo import MongoClient



mongo_database_user='brenden_wds'
mongo_database_pass='Ky4QAoSP5yhSSU5W'
connect = pymongo.MongoClient("mongodb+srv://brenden_wds:Ky4QAoSP5yhSSU5W@cluster0.vvn5s.mongodb.net/wiki?retryWrites=true&w=majority")
# mongodb+srv://brenden_wiki:<password>@cluster0.f5gdl.mongodb.net/<dbname>?retryWrites=true&w=majority