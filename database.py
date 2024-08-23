import sqlite3
from prettytable import PrettyTable

GRADING_SCALE = {"A": 4.00, "A-": 3.67, "B+": 3.33, "B": 3.00, "B-": 2.67, 
                 "C+": 2.33, "C-": 2.00, "C": 2.00, "D": 1.00, "F": 0}
                 

def connect():
    return sqlite3.connect("gpa_data.db")


def add_semester(connection, semester_count):

    query = f"""
    CREATE TABLE IF NOT EXISTS "semester_{semester_count}" (
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        credits INTEGER, 
        grade TEXT
    );
    """

    with connection:
        connection.execute(query)


def add_class(connection, semester_count, name, credits, grade):

    query = f"""
    INSERT INTO "semester_{semester_count}" 
    (name, credits, grade) 
    VALUES (:name, :credits, :grade);   
    """

    with connection:
        connection.execute(query, {"name": name, "credits": credits, "grade": grade})


def display_semester(connection, semester_count):

    query = f"""
    SELECT * FROM "semester_{semester_count}";
    """

    with connection:
        cursor = connection.execute(query)
        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

    table = PrettyTable()
    table.field_names = column_names

    for row in rows:
        table.add_row(row)
    
    return table


def get_semester_tables(connection):
    query = """
    SELECT COUNT(name) FROM sqlite_master
    WHERE type = 'table'
    AND name LIKE 'semester_%';
    """

    cursor = connection.execute(query)
    count = cursor.fetchone()[0]
    return count


def get_semester_gpa(connection, semester_count):    
    query = f"""
    SELECT credits, grade
    FROM "semester_{semester_count}"
    """

    with connection:
        results = connection.execute(query).fetchall()

    quality_points, total_credits = 0, 0
    for row in results:
        quality_points += row[0] * GRADING_SCALE[row[1]]
        total_credits += row[0]
    if total_credits > 0:
        semester_gpa = (quality_points / total_credits)
    else:
        semester_gpa = 0
    return semester_gpa


def get_cumulative_gpa(connection, semester_count):
    quality_points, total_credits = 0, 0
    all_results = []

    with connection:
        for semester in range(1, semester_count + 1):
            query = f"""
            SELECT credits, grade
            FROM "semester_{semester}"
            """
            results = connection.execute(query).fetchall()
            all_results.extend(results)

    for row in all_results:
        quality_points += row[0] * GRADING_SCALE[row[1]]
        total_credits += row[0]
   
    if total_credits > 0:
        cumulative_gpa = (quality_points / total_credits)
    else:
        cumulative_gpa = 0

    return cumulative_gpa