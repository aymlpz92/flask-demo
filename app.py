from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'Hello, World'


@app.route("/data")
def data():
    return jsonify({'name': 'Pikachu', 'power': 20, 'life': 50})