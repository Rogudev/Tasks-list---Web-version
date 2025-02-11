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
@app.route('/add_project', methods=['POST'])
def agregar():
    name = request.form.get('name')
    tasks = load_tasks_list()
    tasks.append({'title': name, 'finalized': False})
    save_tasks_list(tasks)
    return redirect(url_for('index'))

# Update a task as done, the id is for localizing the task in JSON
@app.route('/finalize_task/<int:id>', methods=['GET'])
def finalize_task(id):
    tasks = load_tasks_list()
    tasks[id]['finalized'] = True
    save_tasks_list(tasks)
    return redirect(url_for('index'))

# Delete a task
@app.route('/delete_task/<int:id>', methods=['GET'])
def delete_task(id):
    tasks = load_tasks_list()
    tasks.pop(id)
    save_tasks_list(tasks)
    return redirect(url_for('index'))

# Function to run the Flask app
def run_app():
    app.run(debug=True, host='0.0.0.0', port=app_port, use_reloader=False)


# Endpoint to shutdown the server
@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.kill(os.getpid(), signal.SIGINT)
    return 'App has been stopped'


if __name__ == '__main__':
    # Start the Flask app in a separate thread
    threading.Thread(target=run_app).start()

    # Open the browser after the app starts
    webbrowser.open(f'http://127.0.0.1:{app_port}')
