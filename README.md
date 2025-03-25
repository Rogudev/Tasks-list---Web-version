# 'Task List' Project (web version)

## Overview
This project is an updated version of [To do projects](https://github.com/RodrigoGtzRbl/portfolioProjects/tree/main/To%20Do%20projects%20list), transitioning from a graphical interface to a web interface using Bootstrap styling.


## Requirements
  - `flask`
  - `json`
  - `webbrowser`
  - `threading`
  - `pyinstaller`
  - `os`
  - `signal`
  - `random`
  - `socket`


## Features
- Uses a JSON file as a database.
- Allows changing the status of any task from 'Undone' to 'Done'.
- Allows deleting tasks.
- Allows restarting tasks, from 'Done' to 'Undone'.
- Allows adding new projects to the list with a bootstrap form.
- Allows change the name and the description of task.


## Installation

1. Create a virtual environment (recommended):
  ```bash
    python3 -m venv [env-name]
  ```

2. Clone the repository:
  ```bash
    git clone https://github.com/Rogudev/Tasks-list---Web-version.git
  ```

3. Access the cloned project folder:
  ```bash
    cd Tasks-list---Web-version
  ```

4. Paste the repository files into the venv:
  ```bash
    mv static templates app.py db.json requirements.txt  ../[env-name]
  ```

5. Install the requirements after activating the venv:
  ```bash
    pip install -r requirements.txt
  ```

6. Make the installer
```bash
  pyinstaller --onefile --add-data "db.json:." --add-data "templates:templates" --add-data "static:static" app.py
```

7. Copy the database inside dist directory (this directory is created by pyinstaller)
```bash
  cp db.json dist/
```

8. Make the app executable and run it
```bash
  chmod +x dist/app.py
  ./dist/app.py
```

**NOTE**
Optionally, you can move the dist directory to anywhere you have your path exported and creates an script to execute the app from terminal.
Example for the path _/home/bin/_
```bash
  mkdir -p /home/$USER/bin/task_list_app
  mv dist/* /home/$USER/bin/task_list_app/
  nano /home/bin/task-list
```
Paste this code in nano text editor:
```bash
#!/bin/bash
nohup ~/bin/task_list_app/app > /dev/null 2>&1 &
```

Now you would be allowed to open the app from terminal typing _task-list_


## How it works
1. Create the Flask app
```Python
app = Flask(__name__)
```

2. Create the paths for database file and the port file
```Python
base_path = os.path.dirname(os.path.abspath(__file__))

database_path = os.path.join(base_path, 'db.json')
port_file_path = os.path.join(base_path, 'port.text')
```

3. Functions
- Availability port
```Python
def is_port_available(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # try to bind to the port
        result = s.connect_ex(('127.0.0.1', port))
        # if result == 0, port is in use
        return result != 0
```
- Find a random port
```Python
def find_random_available_port():
    while True:
        # generate a random port between 5000 and 6000
        random_port = random.randint(5000, 6000)
        
        # check availability
        if is_port_available(random_port):
            return random_port  #  if its free, return it, if not, re loop
```

- Read, create and delete the port file
```Python
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
    with open(port_file_path, 'w') as file:
        file.write(str(port))

# del the port file
def delete_port_file():
    """Deletes the port file."""
    if os.path.exists(port_file_path):
        os.remove(port_file_path)
```

- Load the tasks from database
```Python
def load_tasks_list():
    try:
        with open(database_path, 'r') as file:
            tasks = json.load(file)
            tasks.sort(key=lambda x: x['finalized'], reverse=False)

    except FileNotFoundError:
        tasks = []
    return tasks
```

- Save the database
```Python
def save_tasks_list(tasks):
    with open(database_path, 'w') as file:
        json.dump(tasks, file, indent=4)
```

4. Routes definition
- Index
```Python
@app.route('/')
def index():
    tasks = load_tasks_list()
    return render_template('index.html', tasks=tasks)
```

- Task managment
```Python
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
```

- Start and Stop app
**Note**
The host is defined as 127.0.0.1 to only allow the user's connection
```Python
def run_app():
    app.run(debug=True, host='127.0.0.1', port=app_port, use_reloader=False)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    # del the port file     
    delete_port_file()
    os.kill(os.getpid(), signal.SIGINT)
    return 'App has been stopped'
```

- Running when import prevention
```Python
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
```


## License

This project is licensed under the MIT License - see the information below for details.


MIT License

Copyright (c) 2025 Rodrigo Gutierez Ribal [rogudev.com](https://rogudev.com/es)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
