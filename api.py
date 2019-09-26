from flask import Flask, escape, request
import requests 

app = Flask(__name__)

URL = "http://localhost:8890/sparql/?default-graph-uri=http%3A%2F%2Fexample.com&query=select+*+where+%7B+%3Fs+%3Fp+%3Fo%7D&should-sponge=&format=text%2Fturtle&timeout=0&debug=on&run=+Run+Query+"
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    r = requests.get(url = URL) 
    data = r.content 
    # if (request.headers.get('api-key') != 'test'):
    #     return 'error'
    return data