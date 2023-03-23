import pymysql

connection = pymysql.connect(host="127.0.0,1",
                             user="root",
                             password="1cadwaer2", 
                             database="zipcodes")

try:
    cursor = connection.cursor()
    cursor.execute("select database();")
    db = cursor.fetchone()
    print("You're connected to database: ", db)
except pymysql.Error as e:
    print("Error while connecting to MySQL", e)
finally:
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
