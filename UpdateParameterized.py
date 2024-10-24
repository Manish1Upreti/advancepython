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
        print("Database is connected !")

except:
    print("Database unable to Connect !")

myc = conn.cursor()
# using Dictionary
sql = "UPDATE student SET  name=%(na)s, roll=%(ro)s, fees=%(fe)s WHERE stuid=%(id)s"
# keys inside bracket
i = int(input("Enter id in which You want to Update: "))
n = input("Enter Your Name: ")
r = int(input("Enter Your Roll: "))
f = float(input("Enter Your fees: "))
params = {'na':n, 'ro':r, 'fe':f, 'id':i}

# using tuples
# sql = "UPDATE student SET  fees=%s WHERE stuid=%s"
# sid = int(input("Enter the id to update: "))
# fe = float(input("Enter the Updated Fees: "))
# params = (fe, sid)

try:
    myc.execute(sql, params)
    conn.commit()
    print(myc.rowcount, 'Updated Row')
except:
    conn.rollback()
    print("Unable to Update Data")

myc.close()
conn.close()
