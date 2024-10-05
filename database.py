from flask_pymongo import PyMongo
from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Set MongoDB URI in your config
app.config["MONGO_URI"] = "mongodb://localhost:27017/secure_image_cloud"  # Replace with your correct MongoDB URI

# Initialize PyMongo
mongo = PyMongo(app)

# Access the database object
db = mongo.db
