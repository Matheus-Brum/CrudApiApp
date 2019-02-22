import sqlite3

db = sqlite3.connect(':memory:')
cursor = db.cursor()

cursor.execute('''CREATE TABLE Teams (Id integer,Name varchar(20), "
           "Conference varchar(20), City varchar(20), Championships integer)''')
cursor.execute("INSERT INTO Teams VALUES (1, 'Lakers', 'Western', 'Los Angeles', 17)")
cursor.execute("INSERT INTO Teams VALUES (2, 'Clippers', 'Western', 'Los Angeles', 0)")
cursor.execute("INSERT INTO Teams VALUES (3, 'Heat', 'Eastern', 'Miami', 3)")
cursor.execute("INSERT INTO Teams VALUES (4, 'Rockets', 'Western', 'Houston', 2)")
cursor.execute("INSERT INTO Teams VALUES (5, 'Celtics', 'Eastern', 'Boston', 15)")

for row in cursor.execute('SELECT * FROM Teams'):
    print(row)

# FIND QUERY
find_query = cursor.execute('''SELECT * FROM Teams WHERE City LIKE "%Los Angeles%" AND Championships > 0 ''')

for row in find_query:
    print(row)

# SAVE QUERY
save_query = cursor.execute('''UPDATE Teams SET Championships=4 WHERE Name="Heat"''')
for row in cursor.execute('SELECT * FROM Teams'):
    print(row)
