prime=True
divisors=2
number=int(input("Anna kokonaisluku "))
if number > 1:
    for x in range(2,number):
        if number % x == 0:
            prime=False
            divisors+=1
    if prime:
        print("Se on alkuluku")
    else:
        print(f"Se on yhdistetty luku ja sillä on {divisors} jakajaa")
else:
    print("Alkunumeron pitää olla enemmän kuin 1")