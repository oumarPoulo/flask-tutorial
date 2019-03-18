from flask import jsonify, abort, request


from tasks_app.blueprints import tasks_manager

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


@tasks_manager.route('/', methods=['POST'])
def create_task():
    """ add a task to the tasks list """
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


@tasks_manager.route('/', methods=['GET'])
def get_tasks():
    """ Return all the tasks stored """
    return jsonify(tasks)


@tasks_manager.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """ Return task by task Id"""
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task)
    return abort(404)

