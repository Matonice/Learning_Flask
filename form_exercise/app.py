from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/report')
def report():

    username = request.args.get('username')

    upper = any(c.isupper() for c in username)
    lower = any(c.islower() for c in username)
    end_digit = username[-1].isdigit()

    report = upper and lower and end_digit
    return render_template("report.html", upper=upper, lower=lower, end_digit=end_digit, report=report)

if __name__=='__main__':
    app.run(debug=True)
