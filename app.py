from flask import Flask, render_template_string

app = Flask(__name__)

# Quotes dictionary
quotes = {
    "0": "Zero excuses. Start now without wasting time.",
    "1": "One step at a time leads to big success.",
    "2": "Two choices: Give up or grow.",
    "3": "Get up macha , you can",
    "4": "Four walls can't stop a determined mind.",
    "5": "Five minutes of effort beats zero action.",
    "6": "Six times you fall, seven times you rise.",
    "7": "Seven days a week – stay consistent!",
    "8": "Believe in yourself.",
    "9": "Nine lives? No. One life. Make it count!"
}

# Home Page
@app.route("/")
def home():
    return render_template_string("""
        <h1>Select a Number (0-9)</h1>
        {% for num in range(10) %}
            <a href="/quote/{{num}}">
                <button style="margin:5px; padding:10px 15px;">
                    {{num}}
                </button>
            </a>
        {% endfor %}
    """)

# Quote Page
@app.route("/quote/<num>")
def show_quote(num):
    quote = quotes.get(num, "Invalid number Mach !")
    return render_template_string("""
        <h2>Your Motivational Quote:</h2>
        <p style="font-size:20px;">{{quote}}</p>
        <br>
        <a href="/">Go Back</a>
    """, quote=quote)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 