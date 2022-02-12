# from gc import collect
# from matplotlib.collections import Collection
import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://Chimexi42:chimexi42@cluster0.s7yme.mongodb.net/Sample?retryWrites=true&w=majority')

db = cluster['Sample']

collection = db['Sample']

post =  {'name':'chima', 'score': 15}

collection.insert_one(post)
