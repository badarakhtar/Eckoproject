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

