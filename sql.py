import sqlite3

## Connect to sqlite
connection = sqlite3.connect('student.db')

## Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

## Create the table
table_info = """
CREATE TABLE student(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT);
"""

cursor.execute(table_info)

## Insert some records
cursor.execute('''INSERT INTO student VALUES('Eduardo', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO student VALUES('Fernando', 'Data Science', 'B', 100)''')
cursor.execute('''INSERT INTO student VALUES('Meirielle', 'Data Science', 'A', 86)''')
cursor.execute('''INSERT INTO student VALUES('Melissa', 'DEVOPS', 'A', 50)''')
cursor.execute('''INSERT INTO student VALUES('Ivan', 'DEVOPS', 'A', 35)''')

## Display all the records
print('The inserted records are')
data=cursor.execute('SELECT * FROM student')

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()