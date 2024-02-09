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
    cursor.execute(f"SELECT name, municipality FROM airport WHERE ident='{x}'")
    result_row = cursor.fetchall()
    return result_row

#haku=input("Anna ICAO koodi :) ")

print(kanta(input("Anna ICAO koodi :) ")))