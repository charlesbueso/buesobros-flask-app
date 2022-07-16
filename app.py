from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")

def index():
    message = 'Hello world!'
    return render_template("home.html", message = message)

if __name__ == "__main__":
    app.directory='./'
    app.run(host='127.0.0.1', port=5000)