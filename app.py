from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Sakthi Macha ! error in webhook -> ngrok -> jenkins in ubuntu"

app.run(host="0.0.0.0", port=5000)
