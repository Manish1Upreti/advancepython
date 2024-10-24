import mysql.connector

def student(ro):
    try:
        conn = mysql.connector.connect(
            user='root',
            password='9843721190@Manish',
            host='Localhost',
            database='sql_intro',
            port=3306
        )
        if(conn.is_connected()):
         print("Database Connection Success !")
    except:
        print("Database Connection Unsuccessful !")

    myc = conn.cursor()
    sql = "SELECT * FROM student where roll=%(roll)s"


    params = {'roll': ro}

    try:
        myc.execute(sql, params)
        row = myc.fetchone()
        while row is not None:
            print(row)
            row = myc.fetchone()
        print('Total Rows:', myc.rowcount)
    except:
        conn.rollback()
        print('Unable to retrieve data')

    myc.close()
    conn.close()

while True:
    # Data Input from User
    ro = int(input('Enter Roll: '))
    student(ro)
    ans = input('DO to want to exit?(Y/N)')
    if(ans == 'Y'):
        break

