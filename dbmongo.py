from pymongo import MongoClient
from bson import ObjectId

try:
    client = MongoClient()
    db = client['python']
except Exception as e:
    print("Erro:{}".format(e))
    exit()

#print(db.usuario.find_one())

# registro = {"_id":5, "nome":"felipe", "linguagem":"javascript"}
# db.usuario.insert(registro)

# print(db.usuario.find_one({"_id":5}))

#mostrar em uma linha
registros = [x for x in db.usuario.find()]
print(registros)

# Mostrar cada registro numa linha 
# for registro in db.usuario.find():
#     print(registro)

#db.usuario.update({"nome":"daniel"}, {"$set":{"linguagem":"python"}})
#db.usuario.update({"nome":"daniel"}, {"$set":{"_id":1}})

#db.usuario.update({'_id': ObjectId('5be8616cd652bcd4ec3bfee2')},{"$set":"linguagem":"html e css"})

#db.usuario.remove({'_id': ObjectId('5be8616cd652bcd4ec3bfee2')})