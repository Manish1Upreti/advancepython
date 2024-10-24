import mysql.connector
try:
    conn = mysql.connector.connect(
        user='root',
        password='9843721190@Manish',
        host='Localhost',
        database='sql_intro',
        port=3306
    )
    if(conn.is_connected()):
        print("Database connection Success !")
except:
    print("Could not Connect to Database !")

myc = conn.cursor()
#sql = 'DELETE FROM student where stuid=%s' # using tuple
sql = 'DELETE FROM student where stuid=%(id)s'# using dictionary
n = int(input("Enter Std id to Delete: "))
params_del = {'id': n}
try:
    myc.execute(sql, params_del)
    conn.commit()
    print(myc.rowcount, 'Row Deleted')
except:
    conn.rollback()
    print("Unable to Delete Data")
myc.close()
conn.close()
