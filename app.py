from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb+srv://kunalghosh5135:0dVTHIl9bQm2jBYT@cluster0.i83ic20.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["webhook_db"]
collection = db["events"]

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Webhook received")

    payload = {}

    # Handle Push
    if 'pusher' in data:
        payload = {
            "request_id": data['head_commit']['id'],
            "author": data["pusher"]["name"],
            "action": "PUSH",
            "from_branch": None,
            "to_branch": data["ref"].split('/')[-1],
            "timestamp": datetime.utcnow().isoformat()
        }

    # Handle Pull Request
    elif 'pull_request' in data:
        pr = data["pull_request"]
        action_type = "MERGE" if pr.get("merged") else "PULL_REQUEST"

        payload = {
            "request_id": str(pr["id"]),
            "author": pr["user"]["login"],
            "action": action_type,
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"],
            "timestamp": pr["updated_at"]
        }

    if payload:
        collection.insert_one(payload)

    return jsonify({"status": "received"}), 200

@app.route('/events')
def get_events():
    data = list(collection.find().sort("timestamp", -1).limit(10))
    for d in data:
        d["_id"] = str(d["_id"])  # Convert ObjectId to string
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
