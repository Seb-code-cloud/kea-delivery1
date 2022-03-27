#this module is imported to help connect to out SQL database and makes it possible to access and manipulate it 
import mysql.connector

#this function will work as our personal connector, with the users own SQL information. We will use dbconnect() multiple times thourgh our program
def dbconnect():
	connection = mysql.connector.connect(
		host="sela-mysql-4semester.mysql.database.azure.com",
		user="sela",
		password="2021q3-Opmedkop30",
		database="delivery1")
	return connection
