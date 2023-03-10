import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster.tzgxgl3.mongodb.net/Cluster?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20221027',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')
for movie in movies:
    a = movie.select_one('td.title > div > a')
    if a is not None:
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        title = a.text
        star = movie.select_one('td.point').text

        doc = {
            'title':title,
            'rank':rank,
            'star':star
        }
        db.movies.insert_one(doc)