from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster.tzgxgl3.mongodb.net/Cluster?retryWrites=true&w=majority')
db = client.dbsparta

db.movies.update_one({'title':'씽2게더'},{'$set':{'star':str(2)}})
