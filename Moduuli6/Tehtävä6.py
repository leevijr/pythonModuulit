import math

def pizzaEurosPerArea(price, diameter):
    diameter/=100
    
    return price/(diameter**2/4*math.pi)




ekaHinta=float(input("ekan pitsan hinta euroina? "))
ekaHalkaisija=float(input("ekan pitsan halkaisija senttimetreinä? "))
tokaHinta=float(input("tokan pitsan hinta euroina? "))
tokaHalkaisija=float(input("tokan pitsan halkaisija senttimetreinä? "))


ekaArvo=pizzaEurosPerArea(ekaHinta, ekaHalkaisija)
tokaArvo=pizzaEurosPerArea(tokaHinta, tokaHalkaisija)

if ekaArvo<tokaArvo:
    betterValue="Ekalla pitsalla on parempi hinta/määrä suhde."
else:
    betterValue="Tokalla pitsalla on parempi hinta/määrä suhde."
print(f"Ekan pitsan arvo on {ekaArvo :.2f} euroa per neliömetri. Toisen pitsan arvo on {tokaArvo :.2f} euroa per neliömetri. {betterValue}")