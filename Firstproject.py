
import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='9843721190@Manish',
        host='localhost',
        database='sql_intro',
        port=3306
    )
    if (conn.is_connected()):
           print('Connected')
except:
    print("Unable to Connect")

# sql = 'CREATE TABLE student(stuid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(25),roll INT,fees FLOAT)'
# sql = 'INSERT INTO student(name,roll,fees) VALUES ("Krishna", 102,26000),("Hari",103,27000)'
# sql = 'DELETE FROM student where stuid=7'
# sql = 'UPDATE student SET fees=1000 WHERE stuid=9'
sql = 'SELECT * FROM student WHERE roll=102'
# myc = conn.cursor(buffered=True)  # for fetchmany we should have buffered=True
myc = conn.cursor()
try:
    myc.execute(sql)
    #conn.commit()                  # Committing the change in table
    # print(myc.rowcount, "Rows Inserted")
    row = myc.fetchone()   # one by one
    while row is not None:
        print(row)
        row = myc.fetchone()
    print(myc.rowcount)
    # while row is not None:
    #    stuid = row[0]
    #    name = row[1]
    #    roll = row[2]
    #    fees = row[3]
    #    print(f'Stud ID: {stuid} Name: {name} Roll: {roll} Fees: {fees}')
    #    row = myc.fetchone()

    #rows = myc.fetchall()  # all at once
    #for r in rows:
    #   stuid = r[0]
    #   name = r[1]
    #    roll = r[2]
    #    fees = r[3]
    #    print(f'Stud ID: {stuid} Name: {name} Roll: {roll} Fees: {fees}')

    #rows = myc.fetchmany(size=5)  # specific number of rows at once
    #for r in rows:
    #    stuid = r[0]
    #    name = r[1]
    #    roll = r[2]
    #   fees = r[3]
    #    print(f'Stud ID: {stuid} Name: {name} Roll: {roll} Fees: {fees}')

    print('Total Rows:', myc.rowcount)
    # print('Student ID:', myc.lastrowid)
except:
    conn.rollback()             # Rollback the change
    print('Unable to Insert Data')
myc.close()      # Close cursor
conn.close()     # Close Connection
