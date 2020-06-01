from flask import Flask,request,jsonify
from flask_pymongo import PyMongo,ObjectId
from flask_cors import CORS
 
 

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pythonreactdb"
mongo = PyMongo(app)

db= mongo.db.users


@app.route('/users',methods=['POST'])
def createUser():  
     id= db.insert({
         'name':request.json['name'],
         'email':request.json['email'],
         'password':request.json['password']
     })
     return jsonify(str(ObjectId(id)))
     

@app.route('/users',methods=['GET'])
def getUsers():
    users=[]
    for doc in db.find():
        users.append({
            '_id':str(ObjectId(doc['_id'])),
            'email':doc['email'],
            'password':doc['password']
        })
    return jsonify(str(users))

@app.route('/user/<id>',methods=['GET'])
def getUser(id):
    user=db.find_one({'_id':ObjectId(id)})
    print(user)
    return jsonify({
        '_id':str(ObjectId(user['_id'])),
        'email':user['email'],
        'password':user['password']

    })

@app.route('/users/<id>',methods=['GET'])
def deleteUser():
    return 'received'

@app.route('/users/<id>',methods=['PUT'])
def updateUser():
    return 'received'


if __name__ == "__main__":
    app.run(debug=True)