will=int(input("uusi(1), etsi(2) vai lopeta(3) ? :) "))
icao=None
name=None
airports={}
while will<=3 and will>=1:
    if will==1:
        icao=input("Anna icao koodi :) ")
        name=input("Anna lentokentän nimi :) ")
        airports.update({icao: name})
    elif will==2:
        haku=input("Mikä ICAO koodi :) ")
        print(f"{airports[haku]} lentokentällä on ICAO koodi {haku}")
    elif will==3:
        break
    will = int(input("uusi(1), etsi(2) vai lopeta(3) ? :) "))
