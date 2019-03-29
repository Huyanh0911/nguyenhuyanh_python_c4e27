from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
ex4_5 = client.c4e
river = ex4_5["river"]
all_river=river.find(({"continent":"Africa"}))
for rivers in all_river:
    print("Name: ",rivers["name"])
    print("Continent: ",rivers['continent'])
    print("----------------------------")