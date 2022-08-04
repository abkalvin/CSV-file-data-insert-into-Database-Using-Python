import csv
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "School"
)
with open("C:\\Users\hp\Downloads\march18_myspeed.csv\march18_myspeed.csv") as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    # print(type(csvfile))


    all_value = []
    for row in csvfile:
        # print(row[0])

        value = (row[0], row[1], row[2], row[3], row[4], row[5])
        all_value.append(value)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE STUDENTS_1 (Service_Provider VARCHAR(20), Technology VARCHAR(20), Test_type VARCHAR(20), Data_Speed FLOAT, Signal_strength INT,LSA VARCHAR(20))")
query = "insert into `students` (Service_Provider, Technology, Test_type, Data_Speed, Signal_strength,LSA) values(%s, %s, %s, %s, %s, %s)"

mycursor.executemany(query, all_value)
mydb.commit()
print("Inserted successfully")
