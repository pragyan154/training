import mysql.connector

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="c361cohort"
)

cursor = connection.cursor()
create_tablequery = """CREATE TABLE IF not exists table_name1( column1 varchar(255), column2 int)"""

cursor.execute(create_tablequery)
print("table created succesfully")

insert_query = "insert into table_name1 (column1, column2) values(%s,%s)"

data = [("value1", 22),("value2",99)]
cursor.executemany(insert_query,data)

connection.commit()

selectquery = "select * from table_name1"
cursor.execute(selectquery)

rows = cursor.fetchall()

for row in rows:
    print("row: ",row) 

cursor.close()
connection.close()