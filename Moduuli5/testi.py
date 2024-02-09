import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)
"""
cursor = connection.cursor()
cursor.execute("SELECT id FROM game")
result_row = cursor.fetchone()
print(result_row)
"""
cursor2 = connection.cursor()

print(type(cursor2))
print(cursor2)
cursor2.execute("SELECT id FROM game")
print(cursor2)

class MyClass:
    pass


print(MyClass)
print(type(MyClass()))
#result_row = cursor.fetchone()
#print(result_row)