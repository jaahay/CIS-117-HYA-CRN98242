statements = (
    """DROP TABLE IF EXISTS Courses;""",
    """CREATE TABLE Courses(
            id INT AUTO_INCREMENT,
            external_id VARCHAR(255) NOT NULL,
            title VARCHAR(255) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY(id)
        );""",
    """INSERT INTO Courses (external_id, title)
        VALUES
            ("math_1", "Algebra"),
            ("math_2", "Geometry"),
            ("math_3", "Calculus"),
            ("english_1", "Interpretation"),
            ("english_2", "Argumentation")
        ;""",
    """SELECT * FROM COURSES
        WHERE title LIKE 'A%';"""
)

import sqlite3
con = sqlite3.connect('hw15.db')
cur = con.cursor()

for statement in statements:
    print("Executing: ", statement)
    cur.execute(statement)
    for record in cur.fetchall():
        print(record)

def lesson():
    import sqlite3

    con = sqlite3.connect('web.db')

    cur = con.cursor()
    cur.execute("""DROP TABLE IF EXISTS Keywords""")
    cur.execute("""CREATE TABLE Keywords (url text, word text, freq int)""")
    cur.execute("""INSERT INTO Keywords VALUES ('one.html', 'Beijing', 3)""")

    url, word, freq = 'one.html', 'Paris', 5
    cur.execute("""INSERT INTO Keywords VALUES (?, ?, ?)""", (url, word, freq))
    record = ('one.html', 'Chicago', 5)
    cur.execute("""INSERT INTO Keywords VALUES (?, ?, ?)""", record)
    con.commit()
    con.close()

    con = sqlite3.connect('web.db')
    cur = con.cursor()

    cur.execute("""SELECT * FROM Keywords""")
    for record in cur.fetchall():
        print(record)
            # ('one.html', 'Beijing', 3)
            # ('one.html','Paris', 5)
            # ('one.html', 'Chicago', 5)

    cur.execute("""SELECT * FROM Keywords WHERE word = ? AND freq > ?""", (word, 0))
    example = cur.fetchall()
    print(example)

    cur.execute("""DROP TABLE IF EXISTS Books""")
    cur.execute("""CREATE TABLE Books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(id)
            ON DELETE CASCADE
    );""")

    con.close()