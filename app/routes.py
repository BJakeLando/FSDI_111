from flask import Flask, render_template   #from flask module import flask class


app = Flask(__name__)    #Insantiate Flask into app (object)

@app.get("/")           #flask decorator that maps routes to view functions
def index():            #a view function is a function mapped to a route (flask)
    me = {
        "frist_name": "Brandon",
        "last_name":"Landers",
        "hobbies": "surfing",
        "active": True
    }
    return me

@app.get("/about")
def about_me():
    return render_template("index.html")
