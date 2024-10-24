import mysql.connector

def student(nm, ro,fe):
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
    sql = "INSERT INTO student(name, roll, fees) VALUES(%(name)s, %(roll)s, %(fees)s)"


    params = {'name': nm, 'roll': ro, 'fees': fe}

    try:
        myc.execute(sql, params)
        conn.commit()
        print(myc.rowcount, 'New row inserted')
        print(f'Stu ID: {myc.lastrowid} Inserted')
    except:
        conn.rollback()
        print('Unable to Insert Data')

    myc.close()
    conn.close()

while True:
    # Data Input from User
    nm = str(input("Enter Name: "))
    ro = int(input('Enter Roll: '))
    fe = float(input('Enter Fees: '))
    student(nm, ro, fe)
    ans = input('DO to want to exit?(Y/N)')
    if(ans == 'Y'):
        break

