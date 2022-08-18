

# #Sudhanshu sir's server.
# import pymongo
# client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
# db = client.test
# print(db)

import pymongo
client = pymongo.MongoClient("mongodb+srv://anirudhgazelli:7KQ9pwr9BT3MMFam@7heaven.mpm0pax.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "anirudha",
    "email": "anirudhgazelli@gmail.com",
    "surname": "gajelli"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
