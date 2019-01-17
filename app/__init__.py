# This creates an application object as an instance of a class Flask which,
# from flask
from flask import Flask
# This app is an object of Flask and __name__ is passed in so that
app = Flask(__name__)

# Next line is importing routes from app folder
from app import routes_or_views
