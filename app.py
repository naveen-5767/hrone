from flask import Flask, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables from .env if available
load_dotenv()

app = Flask(__name__)

# MongoDB URI from environment or fallback
MONGO_URI = os.getenv("MONGO_URI") or "mongodb+srv://bharathlingathoti:test123@myapicluster.83e3eje.mongodb.net/?retryWrites=true&w=majority&appName=MyAPICluster"

# Connect to MongoDB
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB!")
except Exception as e:
    print("❌ MongoDB connection failed:", e)

# Use sample_mflix database
db = client["sample_mflix"]

# Define collections
collections = {
    "users": db.users,
    "products": db.products,
    "orders":db.orders
}

# Function to create endpoint
def make_endpoint(collection):
    def endpoint_func():
        data = list(collection.find({}, {'_id': 0}).limit(10))
        return jsonify(data)
    return endpoint_func

# Dynamically register routes
for name, coll in collections.items():
    endpoint_url = f"/api/{name}"
    app.add_url_rule(
        endpoint_url,
        endpoint=f"get_{name}",  # ✅ CORRECT: use 'endpoint=', NOT 'name='
        view_func=make_endpoint(coll),
        methods=['GET']
    )

# Root route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Sample Mflix API!",
        "available_endpoints": [f"/api/{name}" for name in collections.keys()]
    })

# Start the app
if __name__ == '__main__':
    app.run(debug=True)
