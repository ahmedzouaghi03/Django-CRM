import mysql.connector 

database = mysql.connector.connect(
	host = 'localhost',
	user =  'root', 
	passwd = 'MYSQLAz04062003' 

	)

#prepare a cursor object 
cursorObject = database.cursor()

#create a database 
cursorObject.execute("CREATE DATABASE newdb")
print("all done!")
