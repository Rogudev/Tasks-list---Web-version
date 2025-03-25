from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import webbrowser
import threading
import os
import signal
import random
import socket
import sys

app = Flask(__name__)

# get the directory of the executable or script
def get_executable_directory():
    """Returns the directory where the executable is located or the script in development."""
    if getattr(sys, 'frozen', False):  # If running as a packaged app
        # When running as a bundled app, use _MEIPASS for the app's temporary directory
        return os.path.dirname(sys.executable)
    else:
        # When running as a script, use the current directory of the script
        return os.path.dirname(os.path.abspath(__file__))

# get actual path
base_path = get_executable_directory()

# create the full path for database and port file
database_path = os.path.join(base_path, 'db.json')
port_file_path = os.path.join(base_path, 'port.text')

def is_port_available(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # try to bind to the port
        result = s.connect_ex(('127.0.0.1', port))
        # if result == 0, port is in use
        return result != 0

def find_random_available_port():
    while True:
        # generate a random port between 5000 and 6000
        random_port = random.randint(5000, 6000)
        
        # check availability
        if is_port_available(random_port):
            return random_port  #  if its free, return it, if not, re loop

# read the portfile if exists, this prevents run multiple apps if the navtab is closed without closing the app
def read_port_from_file():
    """Reads the port from the file if it exists."""
    if os.path.exists(port_file_path):
        with open(port_file_path, 'r') as file:
            port = file.read().strip()
            return int(port) if port.isdigit() else None
    return None

# create the port file
def write_port_to_file(port):
    """Writes the port number to the file."""
    os.makedirs(os.path.dirname(port_file_path), exist_ok=True)
    with open(port_file_path, 'w') as file:
        file.write(str(port))

# del the port file
def delete_port_file():
    """Deletes the port file."""
    if os.path.exists(port_file_path):
        os.remove(port_file_path)

# Function to load from JSON
def load_tasks_list():
    try:
        with open(database_path, 'r') as file:
            tasks = json.load(file)
            tasks.sort(key=lambda x: x['finalized'], reverse=False)

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
def add():
    # get the name from JSON
    data = request.json
    name = data.get('name')
    desc = data.get('desc')

    # load list and append the new task
    tasks = load_tasks_list()
    tasks.append({'title': name, 'finalized': False, 'description': desc})

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

# Update a task
@app.route('/update_task', methods=['POST'])
def update_task():
    # get the id from JSON
    data = request.json
    task_id = data.get('id')
    task_name = data.get('name')
    task_desc = data.get('desc')

    # load list and modify the task using the id
    tasks = load_tasks_list()
    tasks[task_id]['finalized'] = False
    tasks[task_id]['title'] = task_name
    tasks[task_id]['description'] = task_desc

    # save and return
    save_tasks_list(tasks)
    return jsonify({"message": "Task restarted correctly", "status": 200})  # send response

# Function to run the Flask app
def run_app():
    app.run(debug=True, host='127.0.0.1', port=app_port, use_reloader=False)


# Endpoint to shutdown the server
@app.route('/shutdown', methods=['POST'])
def shutdown():
    # del the port file     
    delete_port_file()
    os.kill(os.getpid(), signal.SIGINT)
    return 'App has been stopped'


if __name__ == '__main__':
    # check if the app has been opened before and still running
    app_port = read_port_from_file()

    # check if not exists
    if app_port is None:
    # find the available port
        app_port = find_random_available_port()
        # create the file
        write_port_to_file(app_port)
    
    # start the Flask app in a separate thread
    threading.Thread(target=run_app).start()

    # open the browser after the app starts
    webbrowser.open(f'http://127.0.0.1:{app_port}')
