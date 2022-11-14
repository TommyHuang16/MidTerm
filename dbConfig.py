#!C:\Users\tommy\AppData\Local\Programs\Python\Python310\python.exe
#import mariadb
import mysql.connector 

try:
 	#conn = mariadb.connect(
	conn = mysql.connector.connect(
		user="root",
		password="tommy031103",
		host="127.0.0.1",
		port=3306,
		database="test2",
	)
except: #mariadb.Error as e:
	print("Error connecting to DB")
	exit(1)
cur=conn.cursor()
