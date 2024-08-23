# GPA Calculator

## Video Demo
[Watch the Demo](https://www.youtube.com/watch?v=cKhHTkRwTes)

## Description
The GPA Calculator is a user-friendly tool designed to accurately calculate GPA through a command-line interface. The program presents academic information in a well-organized manner using tables. It stores GPA data in a database so that it can be used for future reference and allows users to easily add new semesters and classes, ensuring that their academic progress is up-to-date. The program also features a menu-driven interface, making navigation straightforward even for those unfamiliar with command-line tools. By providing detailed feedback on user input errors, it improves the overall user experience.

In addition to its core functionality, the GPA Calculator is designed with scalability in mind, allowing for easy updates and modifications. The code structure is modular, with clearly defined functions that can be modified as needed. This makes it a practical tool for current use and also a solid foundation for future enhancements. New users and contributors can quickly understand and navigate the codebase, facilitating seamless collaboration and ongoing development. Whether you're a student looking to track your academic performance or a developer seeking to expand the program’s capabilities, The GPA Calculator offers a reliable and adaptable solution for managing GPA calculations efficiently.

## Installation
Clone the Git repository and set up a virtual environment with the packages specified in `requirements.txt`

1. Clone the git repository:
   ```sh
   git clone <repository-url>
2. Navigate to the project directory:
    ```sh
    cd <repository-directory>
3. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  
    # On Windows, use venv\Scripts\activate
4. Install the required packages:
    ```sh
    pip install -r requirements.txt

## Usage
1. Open a Terminal or Command Line Interface

2. Activate the virtual environment (if not already activated):

    Mac: `source venv/bin/activate`<br> 
    Windows: `venv\Scripts\activate`

3. Execute the Program:

    Within the terminal, start the program by running: `python project.py`

## Features
**Menu-Driven Interface**: Provides a simple command-line menu that guides users through various functionalities such as adding classes, adding semesters, calculating GPA, and getting help.

**Persistent Storage**: Stores your GPA data in a SQLite database, allowing you to retrieve and update your academic records across multiple sessions.

## Project Structure

### .py files:
* project.py: The main script that runs the GPA Calculator. It handles user input, GPA calculation, and interaction with the database.
* database.py: Handles and executes all database operations, including storing and retrieving GPA data using SQLite.
* test_project.py: Performs tests for crucial functions within project.py using Pytest, which is a Python testing framework. This script only runs when it is explicitely called using `pytest test_project.py`

### .db files:
* gpa_data.db: This file will be created when you first run the program using `python project.py`. This is a database file that stores all of your GPA data. NOTE: If this file is deleted, your GPA data will be deleted as well.

### .txt files:
* about.txt: This is a user-friendly file that explains how the GPA Calculator program works and gives users important information on its usage. The contents of this file can be displayed within the program when the user chooses to view it, offering immediate help and instructions while the program is running.
* requirements.txt: This file contains all the necessary packages needed for the program to run accordingly. You can download all the packages within this file by simply running `pip install -r requirements.txt`

### .md files:
* README.md: This file serves as the comprehensive documentation for the GPA Calculator project. It provides essential information and instructions, and it's the very document you are reading right now!