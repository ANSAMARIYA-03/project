from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form["text"]
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment > 0:
        result = "Positive 😊"
    elif sentiment < 0:
        result = "Negative 😡"
    else:
        result = "Neutral 😐"

    return render_template("index.html", text=text, sentiment=result)

if __name__ == "__main__":
    app.run(debug=True)
