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

myc = conn.cursor()
sql = "SELECT * FROM student WHERE roll=%(r)s"  # r is keys

while True:
    n = int(input("Enter student Roll :"))
    # p22arams = (n,)    in tuple
    params = {'r': n}    # n is values in dictionary
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



