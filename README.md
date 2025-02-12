# 'Task List' Project (web version)

## Description
This project is an updated version of [To do projects](https://github.com/RodrigoGtzRbl/portfolioProjects/tree/main/To%20Do%20projects%20list), transitioning from a graphical interface to a web interface using Bootstrap styling.



## Features
- Uses a JSON file as a database.
- Allows changing the status of any task to 'Done'.
- Allows deleting tasks.
- Allows adding new projects to the list with a bootstrap form.



## Requirements
The purpose of the project is to run locally. It contains an example database, and its path is defined in the database_path variable in app.py. You should modify it to the path where your database is located.

Additionally you should install the libraries in your venv using the requirements.txt

- Python 3.x
- Required libraries:
  - `flask`
  - `json`
  - `webbrowser`
  - `threading`
  - `pyinstaller`



## Installation

1. Clone the repository:
  ```bash
    git clone 
  ```

2. Access the project folder:
  ```bash
    cd project-name
  ```

3. Create a virtual environment (recommended):
  ```bash
    python3 -m venv [env-name]
  ```

4. Paste the repository files into the venv:
  ```bash
    mv project-name/* [env-name]
  ```

5. Install the requirements after activating the venv (commands from inside venv):
  ```bash
    source bin/activate
    pip install -r requirements.txt
  ```


## Running

This project is a Flask app with an HTML interface. The style is powered by Bootstrap 5, and the communication between the front-end and back-end is handled using JS AJAX.

The app utilizes several routes, which are triggered by AJAX requests:
- `/add_task`
- `/finalize_task`
- `/delete_task`
- `/restart_task`
- `/shutdown`

These routes are linked to different actions within the app, as follows:

- **Add Task**: The blue "Add" button allows you to add a new task to the list.
- **Close App**: The orange "Close app" button stops the app (shutting down the server and closing the browser tab).
- **Mark as Done**: In the "Done" column, you'll find a blue empty checkbox icon. Clicking it will mark a task as 'Done'.
- **Delete Task**: In the "Delete" column, represented by a red trash can icon, you can remove a task from the list.
- **Restart Task**: In the "Restart" column, represented by a yellow circular arrow icon, you can reset a task's status, unmarking the checkbox.

You can create an executable using PyInstaller by running the following command:
  ```bash
    pyinstaller --onefile --add-data "templates:templates" --add-data "db.json:db.json" app.py
  ```
This will generate a dist folder containing the executable. If you don't already have a db.json file, don't worry! You can simply add a task, and the app will automatically create the db.json file in the folder defined in database_path in app.py .



### Customizing the Database Path

If you'd like to store your database in a different location (e.g., on your desktop), you can modify the database_path variable in the code to point to a different directory, such as:

  database_path = "/home/user/.databases/taskListDB.json"



### Moving the Executable

Alternatively, you can rename the dist folder and move it to another location (e.g., /home/user/.personalApps/). To make it easily accessible from your desktop environment, you can create a .desktop file that links to the executable, if you decided to do this, make sure to create correctly the database_path




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
