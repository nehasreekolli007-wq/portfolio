import sqlite3

conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL
)
""")
count = cursor.execute(
    "SELECT COUNT(*) FROM projects"
).fetchone()[0]

if count == 0:
    projects = [
        (
            "AI Resume Screening System",
            "Developed a web application that analyzes resumes, identifies missing skills, provides suggestions, and predicts suitable job roles."
        ),
        (
            "Personal Portfolio Website",
            "A full-stack portfolio website built using Flask, HTML, CSS, and SQLite."
        ),
        (
            "Farmer Friendly",
            "An AI-powered platform that detects crop diseases, recommends pesticides, and provides agricultural assistance."
        )
    ]

    cursor.executemany(
        "INSERT INTO projects(title, description) VALUES (?, ?)",
        projects
    )


conn.commit()
conn.close()

print("Database created successfully!")