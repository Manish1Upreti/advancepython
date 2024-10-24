import mysql.connector
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
# params = ("Shabnam", 506, 4000)
seq_of_params = [("Raju", 509, 4000), ("Kaju", 504, 800), ("Haju", 507, 40007)]
try:
    myc.executemany(sql, seq_of_params)
    conn.commit()
    print(myc.rowcount, 'Row Inserted')
except:
    conn.rollback()
    print('Unable to Insert Data')

myc.close()
conn.close()
