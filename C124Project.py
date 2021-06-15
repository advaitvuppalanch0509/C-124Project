from flask import Flask,jsonify, request

app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'name': u'Human',
        'contact': u'0821131140', 
        'done': False
    },

    {
        'id': 2,
        'name': u'Dog',
        'contact': u'0415741570', 
        'done': False
    },

    {
        'id': 3,
        'name': u'Cat',
        'contact': u'0312031200', 
        'done': False
    },

    {
        'id': 4,
        'name': u'Cow',
        'contact': u'3152331523', 
        'done': False
    },

    {
        'id': 5,
        'name': u'Goat',
        'contact': u'71512021517', 
        'done': False
    },
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data")
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })


@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 


if (__name__ == '__main__'):
    app.run()