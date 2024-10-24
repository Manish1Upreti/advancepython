# prepared statement is used to execute the same statement repeatedly
# with high efficiency

import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='9843721190@Manish',
        host='Localhost',
        database='sql_intro',
        port=3306
    )
    if (conn.is_connected()):
        print("Database is Connected")

except:
    print("Unable to connect Database !!")

myc = conn.cursor(prepared=True)
# sql = "SELECT * FROM student WHERE roll=?"
sql = "SELECT * FROM student WHERE roll=%s"


while True:
    n = int(input("Enter student Roll :"))
    params = (n,)
    try:
        myc.execute(sql, params)
        row = myc.fetchone()
        while row is not None:
            print(row)
            row = myc.fetchone()
        print('Total Rows:', myc.rowcount)
    except:
        print("Unable to Retrieve Data")

    ans = input('DO to want to exit?(Y/N)')
    if (ans == 'Y'):
        break

myc.close()
conn.close()



