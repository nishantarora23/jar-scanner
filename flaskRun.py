# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
