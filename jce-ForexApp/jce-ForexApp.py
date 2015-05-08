from flask import Flask, render_template
import requests
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/getPrice/')
def getPrice():


if __name__ == '__main__':
    app.run()
