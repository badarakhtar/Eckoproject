import sqlite3

connection = sqlite3.connect("attendance.db")

cursor = connection.cursor()

sqlCommand = '''create table if not exists attendance(
            rollNo integer,
            fname varchar(20),
            lname text,
            day date,
            status char(1));
'''
print('attendance database created successfully')
cursor.execute(sqlCommand)

# connection.commit()
#
# connection.close()
