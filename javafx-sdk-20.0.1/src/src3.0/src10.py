import mysql.connector



mydb = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='password',
	database='people'
)

print(mydb)



# CREATE TABLE `people`.`people` (`fname` VARCHAR(128) NOT NULL, `lname` VARCHAR(128) NULL, `timestamp` DATETIME NULL, PRIMARY KEY (`fname`));



# Create new people records
mycursor = mydb.cursor()
sql = 'INSERT INTO people (fname, lname, timestamp) VALUES (%s, %s, now())'
val = ('Kent', 'Brockman')
mycursor.execute(sql, val)
print(mycursor.rowcount, 'record inserted.')

sql = 'INSERT INTO people (fname, lname, timestamp) VALUES (%s, %s, now())'
val = ('Bunny', 'Easter')
mycursor.execute(sql, val)
print(mycursor.rowcount, 'record inserted.')

sql = 'INSERT INTO people (fname, lname, timestamp) VALUES (%s, %s, now())'
val = ('Doug', 'Farrell')
mycursor.execute(sql, val)
print(mycursor.rowcount, 'record inserted.')

mydb.commit()



# Retrieve all people records
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM people")
myresult = mycursor.fetchall()

for x in myresult:
	print(x)
