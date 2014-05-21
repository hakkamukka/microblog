from flask import Flask

# Creates an applicatino object of class Flask
# and then imports the views module.

# Views are handlers that respond to requests from web browsers.
# In Flask, they are written as Python functions.
app = Flask(__name__)
from app import views
