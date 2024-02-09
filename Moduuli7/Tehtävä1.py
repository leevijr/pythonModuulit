month = int(input("Anna kuukauden  numero :)"))
months =["talvi","kevät","kesä","syksy"]

if month >= 1 and month <= 3:
    print(f"{month} kuukausi on {months[0]}kuukausi")

elif month >= 4 and month <= 6:
    print(f"{month} kuukausi on {months[1]}kuukausi")

elif month >= 7 and month <= 9:
    print(f"{month} kuukausi on {months[2]}kuukausi")

elif month >= 10 and month <= 12:
    print(f"{month} kuukausi on {months[3]}kuukausi")