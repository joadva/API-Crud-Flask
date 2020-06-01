from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
 
 

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/pythonreactdb"
mongo = PyMongo(app)

db= mongo.db.users


@app.route('/users')
def index():
  return '<h1>Corriendo el servidor</h1>'



if __name__ == "__main__":
    app.run(debug=True)