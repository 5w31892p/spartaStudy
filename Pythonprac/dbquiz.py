from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

a_movie = db.movies.find_one({'title':'매트릭스'})
a_star = a_movie['star']

a_movies = list(db.movies.find({'star':a_star},{'_id':False}))
for a in a_moviess:
    print(a['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':str(0)}})