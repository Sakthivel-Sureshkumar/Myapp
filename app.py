from flask import Flask, render_template_string

app = Flask(__name__)

# Quotes dictionary
quotes = {
    "0": "Zero excuses. Start now without wasting time.",
    "1": "One step at a time leads to big success.",
    "2": "Two choices: Give up or grow.",
    "3": "Three words: You got this!",
    "4": "Four walls can't stop a determined mind.",
    "5": "Five minutes of effort beats zero action.",
    "6": "Six times you fall, seven times you rise.",
    "7": "Seven days a week – stay consistent!",
    "8": "Eight letters: Believe in yourself.",
    "9": "Nine lives? No. One life. Make it count!"
}

# Home Page
@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Number Selector</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: white;
            }

            .container {
                text-align: center;
            }

            h1 {
                font-size: 40px;
                margin-bottom: 30px;
            }

            .btn {
                padding: 15px 22px;
                margin: 8px;
                font-size: 18px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: 0.3s ease;
                background: white;
                color: #2a5298;
                font-weight: bold;
            }

            .btn:hover {
                transform: scale(1.1);
                background: #ffcc00;
                color: black;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Select a Number (0-9)</h1>

            {% for num in range(10) %}
                <a href="/quote/{{num}}">
                    <button class="btn">{{num}}</button>
                </a>
            {% endfor %}
        </div>
    </body>
    </html>
    """)
# Quote Page
@app.route("/quote/<num>")
def show_quote(num):
    quote = quotes.get(num, "Invalid number Mach!")
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #000428, #004e92);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: white;
                text-align: center;
            }

            .card {
                background: rgba(255,255,255,0.1);
                padding: 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
            }

            a {
                color: #ffcc00;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Your Motivational Quote</h2>
            <p style="font-size:22px;">{{quote}}</p>
            <br>
            <a href="/">← Go Back</a>
        </div>
    </body>
    </html>
    """, quote=quote)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)