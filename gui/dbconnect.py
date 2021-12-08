import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="carreg"
)

mycursor = mydb.cursor()
sql = "SELECT regid, brand, model, year FROM car"
mycursor.execute(sql)
myresult = mycursor.fetchall()

print(myresult)