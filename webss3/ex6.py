from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
ex6 = client.c4e
river = ex6["river"]
all_river=river.find(({"continent":"S. America"}))

for rivers in all_river:
    length=rivers["length"]
    if length<1000:
        print("Name: ",rivers["name"])
        print("Continent: ",rivers['continent'])
        print("Lenght: ",rivers['length'])
        print("----------------------------")