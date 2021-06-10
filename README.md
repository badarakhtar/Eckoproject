# Eckoproject

The project is done in python with sqlite3 database. 

The following python files are created:
1. Attendance.py -> The command for table creation is done in this file. 
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

2. InputData.py -> This file contains code for inserting values in the table. The stu.csv file which was given in the instructor notes is parsed into the function and the record was split with ','.
import sqlite3
import datetime


def insert(rollNo, fname, lname, day, status):
    conn = sqlite3.connect('attendance.db')
    cur = conn.cursor()
    #print(rollNo, fname, lname, day, status)
    cur.execute('insert into attendance values(?,?,?,?,?)', (rollNo, fname, lname, day, status))
    conn.commit()
    conn.close()

def parse(csvFile):
    table = []
    with open(csvFile, "r") as csvfile:
        for line in csvfile:
            line = line.rstrip()
            columns = line.split(',')
            table.append(columns)
    return table

def record(table):
    for col in table:
        r = int(col[0])
        f = str(col[1])
        l = str(col[2])
        d = (col[3].strip()).split('-')
        day = int(d[0])
        mon = int(d[1])
        yr = int(d[2])
        dat = datetime.date(yr,mon,day)
        s = str(col[4])
        insert(r,f,l,dat,s)

table = parse('stu.csv')

record(table)

print('Record inserted Successfully')

3. StudentInfo.py -> This file contains the code for fetching the record by the roll number provided. The exceptions are properly handled and the modified code does not show error while executing.
import sqlite3

try:
    roll = input("Enter Roll No of Student: ")

    if len(roll) == 0:
        print("Please enter the roll Number")
    else:
        rollNo = int(roll)

        def view(rollNo):
            conn = sqlite3.connect('attendance.db')
            cursor = conn.cursor()
            cursor.execute("select * from attendance where rollNo= ?  ", (rollNo,))
            global data
            data = cursor.fetchall()
            #rowCount = cursor.rowcount
            if not data:
                print("Roll No. not found")
            else:
                print(data)
            # print(cursor.fetchall())


        def feed(data):
            f = open('StudentInfoBy_RollNo.csv', 'w')
            for row in data:
                for col in row:
                    f.write(str(col))
                    f.write(',')
                f.write('\n')
            f.close()


        view(rollNo)
        feed(data)
except ValueError:
    print("Enter Roll No as Number")

finally:
    print("Try for another rollNo")

4. MonthAttendance -> This file contains code for fetching the records of a particular month from the attendance table. The start and end date are hard coded in the program.
import sqlite3
import datetime

# rollNo = int(input("Enter roll No: "))
# month = int(input("Enter month in digits: "))
# year = int(input("Enter year: "))

def view():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    sdate = datetime.date(2018, 4, 1)
    edate = datetime.date(2018,4,30)
    cursor.execute('select * from attendance where day>=? and day<=?', (sdate, edate))
    global data
    data = cursor.fetchall()
    #print(data)

def feed(data):
    f = open('SudentInfoBy_Month.csv', 'w')
    for row in data:
        for col in row:
            f.write(str(col))
            f.write(',')
        f.write('\n')
    f.close()

view()
feed(data)

print('Record fetched Successfully')

5. YearlyAttendance -> This file contains code to fetch the record based on a particular year a unique roll no. The exceptions and errors are properly handled.
import sqlite3
import datetime

try:
    r = input("Enter RollNo: ")
    y = input("Enter year: ")
    if len(r) == 0:
        print("Roll No is not entered")
    if len(y) == 0:
        print("Year is not entered")
    else:
        rollNo = int(r)
        year = int(y)

        def view(rollNo, year):
            sdate = datetime.date(year,1,1)
            edate = datetime.date(year,12,31)
            conn = sqlite3.connect('attendance.db')
            cursor = conn.cursor()
            cursor.execute('select * from attendance where rollNo = ? and day>=? and day<=?', (rollNo,sdate,edate))
            global data
            data = cursor.fetchall()
            if not data:
                print("Roll No. or year not found")
            else:
                print(data)

        def feed(data):
            file = open('StudentInfoBy_Year.csv', 'w')
            for row in data:
                for col in row:
                    file.write(str(col))
                    file.write(',')
                file.write('\n')
            file.close()

        view(rollNo, year)
        feed(data)

except ValueError:
    print("Roll No. and year should be given in numbers")

In order to automatically run on windows operating system having python installed various bat files are created. They are as follows:
 a) database.bat : To automatically create the attendance table if not already created.
 b) import_to_db.bat : To automatically insert values in the attendance table.
 c) monthly_extract.bat : To automatically fetch the record in the monthly duration and store it 
     in the csv format.
 d) student_extract.bat : To automatically fetch the record of a student based on the roll no. 
     given and store it in the csv format.
 e) yearly_extract.bat : To automatically fetch the record of a student based on the roll no. 
     and the year given and store it in the csv format.


