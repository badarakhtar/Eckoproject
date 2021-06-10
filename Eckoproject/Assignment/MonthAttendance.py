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