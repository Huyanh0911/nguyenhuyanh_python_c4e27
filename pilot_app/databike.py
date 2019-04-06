from pymongo import MongoClient
from bson.objectid import ObjectId
from faker import Faker
from random import randint, choice
faker=Faker()
# B1.Conect mongo
mongo_uri= "mongodb+srv://admin:admin@cluster0-i9y1y.mongodb.net/test?retryWrites=true"
client=MongoClient(mongo_uri)

# B2. Get/Creat database
db_bikes = client.bike

# B3. Get/Creat collection
bike_collection = db_bikes["mybike"]

all_bike = bike_collection["Bikes"]
# for i in range(15):
#     new_bike = {
#         "Model":choice(["Honda","Tottem","Giant","Titan"]),
#         "Daily_Fee":choice(["1000000","15000000"]),
#         "Image":choice(["http://giant.vn/","http://honda.vn/"]),
#         "Year":randint(2015,2019),
        
        
#     }
#     all_bike.insert_one(new_bike)
#     print("Saving document{0}.....,".format(i+1))