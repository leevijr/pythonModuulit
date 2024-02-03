def benzin(volume):
    return volume*3.785


convert=input("Montako gallonia? ")
try:
    while convert:
        convert=float(convert)
        if convert<0:
            break
        print(f"{convert} gallonia on {benzin(convert)} litraa")
        convert=input("Montako gallonia? ")

except:
    print("SYÖTÄ NUMEROITA!")