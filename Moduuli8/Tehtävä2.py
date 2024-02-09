import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)
def kanta(x):
    cursor = connection.cursor()
    cursor.execute(f"SELECT COUNT(type), type FROM airport WHERE iso_country='{x}' GROUP BY type")
    result_row = cursor.fetchall()
    return result_row

haku=input("Anna maakoodi :) ")
print(kanta(haku))
