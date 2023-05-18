from flask import Flask, request        # from the flask module import the Flask class

app = Flask(__name__)                   # instantiate the Flask class into app (now an object)

mylist = []

@app.get("/aboutme")                           # Flask decorator that maps a route to a view function. (@ = decorator) (.get = METHOD belongs to app)
def index():                            # a wrapped function is a view function in Flask
    me = {
        "first_name": "Weeraphot",
        "last_name": "Bumbaugh",
        "hobbies": "polevaulting",
        "is_active": True
    }
    return me                           # when you return a dictionary from a flask view function, flask will automatically convert it to JSON

@app.post("/")
def create_entry():
    raw_data = request.json
    mylist.append(raw_data)
    return "", 204

@app.get("/entries")
def get_entries():
    return mylist