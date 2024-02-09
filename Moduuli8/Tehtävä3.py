import mysql.connector
import geopy.distance

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
    cursor.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{x}'")
    result_row = cursor.fetchall()
    return result_row


eka=input("Anna eka ICAO koodi :) ")
eka=kanta(eka)
toka=input("Anna toka ICAO koodi :) ")
toka=kanta(toka)
if eka and toka:
    print(geopy.distance.geodesic(eka, toka).km)

else:
    print("Ei löytynyt lentokenttiä :(")