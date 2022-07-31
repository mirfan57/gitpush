import pymongo
client = pymongo.MongoClient("mongodb+srv://mirfan:mirfan57@cluster0.yo5c4.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"mohai",
    "surname":"nkda",
    "email":"mohai@ineea.com"
}

db1 = client['mongodb']
coll = db1['test']
coll.insert_one(d)