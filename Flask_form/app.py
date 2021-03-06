from flask import Flask, render_template, request
import re
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template("thank_you.html", first=first, last=last)

if __name__ == '__main__':
    app.run(debug=True)
