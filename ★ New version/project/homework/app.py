from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster.tzgxgl3.mongodb.net/Cluster?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }
    db.homework.insert_one(doc)
    return jsonify({'msg':'응원 남기기 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    guest_book = list(db.homework.find({}, {'_id': False}))
    return jsonify({'all_guest':guest_book})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)