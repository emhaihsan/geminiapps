import sqlite3

## connect to the database
conn = sqlite3.connect('student.db')

## create a cursor, which is used to execute SQL queries
c = conn.cursor()

## create table
table_info = """
CREATE table STUDENT
(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25), 
    MARKS INT
)
"""

c.execute(table_info)

## insert some more records
c.execute("INSERT INTO STUDENT VALUES ('Bob', 'Data Science', 'A', 90)")
c.execute("INSERT INTO STUDENT VALUES ('Alice', 'Data Science', 'B', 80)")
c.execute("INSERT INTO STUDENT VALUES ('John', 'Data Science', 'C', 70)")
c.execute("INSERT INTO STUDENT VALUES ('Jane', 'DEVOPS', 'D', 60)")
c.execute("INSERT INTO STUDENT VALUES ('Mark', 'DEVOPS', 'E', 50)")

# display all the records
print("The inserted records are")

data = c.execute("SELECT * FROM STUDENT")
for d in data:
    print(d)

# close the connection
conn.commit()
conn.close()
