from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    task = {
        id: tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json['description'],
        'done': False
    }

    tasks.append(task)

    return jsonify({'task': task}), 201


@app.route('/api/v1/tasks', methods=['GET'])
def get_tasks():
    """ Return all the tasks stored """
    return jsonify(tasks)


@app.route('/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """ Return task by task Id"""
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task)
    return abort(404)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/salvador')
def salvador():
    return "Hello, Salvador"


if __name__ == '__main__':
    app.run()
