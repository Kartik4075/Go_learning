from flask import Flask, jsonify

app = Flask(__name__)

name = {"first" : "Unkown", "last": "Human" }

@app.route("/")
def hello_world():
    return jsonify(name)

@app.route("/kartik")
def hel_world():
    return "<h1> Kartik Nikam </h1> <p>Hello, I am Kartik</p>"  

    print ('Hello_World'!)