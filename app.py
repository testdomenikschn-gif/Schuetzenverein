from flask import Flask, render_template
import os
import re

app = Flask(__name__)

def sort_key(name):
    match = re.search(r'\d+', name)
    return int(match.group()) if match else 0

@app.route("/")
def home():
    folder = "static/bilder"

    bilder = [
        f for f in os.listdir(folder)
        if f.endswith((".jpg", ".png", ".jpeg", ".webp"))
    ]

    bilder = sorted(bilder, key=sort_key)

    return render_template("index.html", bilder=bilder)

if __name__ == "__main__":
    app.run(debug=True)
