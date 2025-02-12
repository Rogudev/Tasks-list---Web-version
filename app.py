from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import webbrowser
import threading
import os
import signal

app = Flask(__name__)

database_path = 'db.json'
app_port = 5588

# Function to load from JSON
def load_tasks_list():
    try:
        with open(database_path, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save projects into JSON
def save_tasks_list(tasks):
    with open(database_path, 'w') as file:
        json.dump(tasks, file, indent=4)

# Index
@app.route('/')
def index():
    tasks = load_tasks_list()
    return render_template('index.html', tasks=tasks)

# Add a new project
@app.route('/add_task', methods=['POST'])
def agregar():
    # get the name from JSON
    data = request.json
    name = data.get('name')

    # load list and append the new task
    tasks = load_tasks_list()
    tasks.append({'title': name, 'finalized': False})

    # save list again
    save_tasks_list(tasks)

    return jsonify({"message": "Task added successfully", "status": 200})  # send response

# Update a task as done, the id is for localizing the task in JSON
@app.route('/finalize_task', methods=['POST'])
def finalize_task():
    # get the id from JSON
    data = request.json
    task_id = data.get('id')

    # load list and modify the task using the id
    tasks = load_tasks_list()
    tasks[task_id]['finalized'] = True

    # save and return
    save_tasks_list(tasks)
    return jsonify({"message": "Task finalized correctly", "status": 200})  # send response

# Delete a task
@app.route('/delete_task', methods=['POST'])
def delete_task():
    # get the id from JSON
    data = request.json
    task_id = data.get('id')

    # drop task using index
    tasks = load_tasks_list()
    tasks.pop(task_id)

    save_tasks_list(tasks)
    return jsonify({"message": "Task deleted correctly", "status": 200})  # send response

# Delete a task
@app.route('/restart_task', methods=['POST'])
def restart_task():
    # get the id from JSON
    data = request.json
    task_id = data.get('id')

    # load list and modify the task using the id
    tasks = load_tasks_list()
    tasks[task_id]['finalized'] = False

    # save and return
    save_tasks_list(tasks)
    return jsonify({"message": "Task restarted correctly", "status": 200})  # send response

# Function to run the Flask app
def run_app():
    app.run(debug=True, host='0.0.0.0', port=app_port, use_reloader=False)


# Endpoint to shutdown the server
@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.kill(os.getpid(), signal.SIGINT)
    return 'App has been stopped'


if __name__ == '__main__':
    # art the Flask app in a separate thread
    threading.Thread(target=run_app).start()

    # open the browser after the app starts
    webbrowser.open(f'http://127.0.0.1:{app_port}')
