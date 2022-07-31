import pymongo
client = pymongo.MongoClient("mongodb+srv://mirfan:mirfan57@cluster0.yo5c4.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"mohai",
    "surname":"nkda",
    "email":"mohai@ineea.com"
}

d = {
    "name":"maverick",
    "surname":"vinales",
    "email":"maverick@moto.com"
}

d = {
    "name":"eden",
    "surname":"hazard",
    "email":"hazard7@real.com"
}

d = {
    "name":"toni",
    "surname":"kroos",
    "email":"toni@real.com"
}

d = {
    "name":"kairm",
    "surname":"benzema",
    "email":"karim@madr.com"
}

db1 = client['mongodb']
coll = db1['test']
coll.insert_one(d)