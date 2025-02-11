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
You can create an executable using PyInstaller by running the following command:
  ```bash
    pyinstaller --onefile --add-data "templates:templates" --add-data "db.json:db.json" app.py
  ```
This will generate a dist folder containing the executable. If you don't already have a db.json file, don't worry! You can simply add a task, and the app will automatically create the db.json file in the same folder.


### Customizing the Database Path
If you'd like to store your database in a different location (e.g., on your desktop), you can modify the database_path variable in the code to point to a different directory, such as:

  database_path = "/home/user/.databases/taskListDB.json"


### Moving the Executable
Alternatively, you can rename the dist folder and move it to another location (e.g., /home/user/.pythonApps/). To make it easily accessible from your desktop environment, you can create a .desktop file that links to the executable.


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
