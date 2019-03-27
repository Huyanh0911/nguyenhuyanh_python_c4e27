from matplotlib import pyplot
from pymongo import MongoClient
mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)

data = client.get_database()

customers = data['customers']
ads = 0
wom = 0 
event = 0

all_cust = list(customers.find())

for customer in all_cust :
    if customer['ref'] == 'events' :
        event = event +1
    elif customer['ref'] == 'wom' :
        wom = wom + 1 
    else : 
        ads = ads + 1
print('event = ',event)
print('wom = ',wom)
print('ads = ',ads)

ref_type = [event,wom,ads]

ref_name = ['events','wom','ads']


pyplot.pie(ref_type , labels = ref_name, autopct='%.1f%%',explode=[0,0.2,0.1] )
pyplot.title('Customers')
pyplot.axis('equal')
pyplot.show()