import mysql.connector
def  student_data(n, r, f):
    try:
        conn = mysql.connector .connect(
            user='root',
            password='9843721190@Manish',
            host='Localhost',
            database='sql_intro',
            port=3306
        )
        if(conn.is_connected()):
            print('Connected')

    except:
        print("Unable to connect")

    sql = "INSERT INTO student(name, roll, fees) VALUES(%s,%s,%s)"
    myc = conn.cursor()
    params = (n, r, f)
    try:
        myc.execute(sql, params)
        conn.commit()
        print(myc.rowcount, 'Row Inserted')
        print(f'Stu ID: {myc.lastrowid} Inserted')
    except:
        conn.rollback()
        print('Unable to Insert Data')

    myc.close()
    conn.close()

while True:
    # Input from user
    nm = input('Enter Name: ')
    ro = int(input('Enter Roll: '))
    fe = float(input('Enter Fees:'))
    student_data(nm, ro, fe)
    ans = input('Do You want to exit?(y/n)')
    if(ans == 'y'):
        break
