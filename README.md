# webhook-repo
# GitHub Webhook Listener

This is a Flask-based webhook listener app for GitHub. It receives GitHub actions (Push, Pull Request, Merge) via webhooks, stores the data in MongoDB Atlas, and displays them in a frontend UI.

## Features
- ✅ Listens to GitHub Webhooks (Push, Pull Request, Merge)
- ✅ Stores data in MongoDB using the schema:
  - request_id
  - author
  - action
  - from_branch
  - to_branch
  - timestamp
- ✅ Frontend updates every 15 seconds with clean, stacked event cards
- ✅ MongoDB Atlas cloud integration

## How to Run

# Clone repo and enter
git clone https://github.com/YOUR_USERNAME/webhook-repo.git
cd webhook-repo

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Flask server
python app.py

ngrok http 5000


<img width="1464" alt="image" src="https://github.com/user-attachments/assets/ca92e210-6dd7-4ebf-961a-df6252ffb1c2" /><img width="988" alt="image" src="https://github.com/user-attachments/assets/19f52b20-2044-433e-a4d5-6e2934ad46da" />
<img width="957" alt="image" src="https://github.com/user-attachments/assets/e8fc4929-f07c-449e-82bf-e2673466ecbd" />


