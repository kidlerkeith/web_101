from flask import Flask
app=Flask(__name__)
@app.route("/")
def home_page():
    return"hello world"


@app.route("/about")
def about():
    return "this is the about page"