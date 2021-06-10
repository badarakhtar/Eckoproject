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





