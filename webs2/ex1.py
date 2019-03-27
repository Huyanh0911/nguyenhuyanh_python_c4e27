from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)

ex1 = client.c4e
comment = ex1["posts"]

document = {
    "title": "Góp ý",
    "author": "Nguyen Huy Anh",
    "content": "Em khong biet noi gi :)"
}
comment.insert_one(document)