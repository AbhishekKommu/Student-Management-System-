from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection
def get_db():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn


# Create table
def create_table():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Get all students
@app.route("/students", methods=["GET"])
def get_students():

    conn = get_db()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return jsonify([dict(student) for student in students])


# Add student
@app.route("/students", methods=["POST"])
def add_student():

    data = request.json

    name = data["name"]
    age = data["age"]
    course = data["course"]
    email = data["email"]

    conn = get_db()

    conn.execute("""
        INSERT INTO students (name, age, course, email)
        VALUES (?, ?, ?, ?)
    """, (name, age, course, email))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student added successfully"
    })


# Delete student
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Student deleted successfully"
    })


# Start application
if __name__ == "__main__":

    create_table()

    app.run(debug=True)
