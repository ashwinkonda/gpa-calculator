import pytest
import os
import project
from project import about, add_class, add_semester, calculate_gpa, goodbye

def test_about_no_file():
    assert about("does_not_exist_file.txt") == False


def test_about_empty_file():
    # Create the file
    with open("empty_file.txt", "w") as file:
        pass
    
    # Perform the test
    assert about("empty_file.txt") == False

    # Clean up
    if os.path.exists("empty_file.txt"):
        os.remove("empty_file.txt")


def test_about_valid_file():
    # Create the file
    with open("non_empty_file.txt", "w") as file:
        file.write("Hello, world!")

    # Perform the test
    assert about("non_empty_file.txt") == True

    # Clean up
    if os.path.exists("non_empty_file.txt"):
        os.remove("non_empty_file.txt")

def test_add_class(mocker):
    assert add_class(semester_count=0) == False

    mocker.patch("builtins.input", side_effect=["Chemistry", "4", "A"])
    mock_database_add_class = mocker.patch("database.add_class")

    semester_count = 1
    assert add_class(semester_count) == True

    mock_database_add_class.assert_called_once_with(mocker.ANY, semester_count, "Chemistry", 4, "A")

def test_add_semester(mocker):
    mock_database_add_semester = mocker.patch("database.add_semester")
    initial_semester_count = 3

    mocker.patch("project.semester_count", initial_semester_count)

    new_semester_count = add_semester()

    mock_database_add_semester.assert_called_once_with(mocker.ANY, initial_semester_count + 1)

    assert new_semester_count == initial_semester_count + 1
    assert project.semester_count == initial_semester_count + 1

def test_calculate_gpa(mocker):
    assert calculate_gpa(semester_count=0) == False

    mocker.patch("database.display_semester", return_value="Sample Semester Table")
    mocker.patch("database.get_semester_gpa", return_value=4.0)
    mocker.patch("database.get_cumulative_gpa", return_value=3.5)
    assert calculate_gpa(semester_count=1) == True

def test_goodbye(mocker):
    mocker.patch("builtins.input", side_effect=["y"])
    assert goodbye(semester_count=1) == True
    assert goodbye(semester_count=0) == False
