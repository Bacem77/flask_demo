from flask import Flask,request
import os
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="color:RED">Hello, World! this website lets you calculate the sum of two numbers.<br> You can do that by entering an url containing the first and second parameters as routes like shown in this exemple :<br> https://flask-demo-cicd.herokuapp.com/5/5 .</h1>'

@app.route("/<a>/<b>/")
def calculate(a=None,b=None):
    sum = "NONE"
    if a and b:
        sum = str((int(a)+int(b)))
    return "<h1>The sum is "+ sum + "</h1>"

def sum(a,b):
    return a+b
if __name__ == '__main__':
    port = os.environ.get("PORT",5000)
    app.run(debug=False,host='0.0.0.0', port=port)