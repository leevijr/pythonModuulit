tyhjaMerkki=True
numbers=[]
while tyhjaMerkki:
    number=input("Anna numero ")
    if number:
        try:
            number=int(number)
            numbers.append(number)
        except:
            pass
    else:
        tyhjaMerkki=False

numbers.sort(reverse=True)

counter=0
for x in numbers:
    counter+=1
    print(x)
    if(counter==5):
        break