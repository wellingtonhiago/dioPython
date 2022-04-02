#Convertendo uma str em um int para a condicional
number = int(input("Number: "))

if number > 0:
    print("{} is positive".format(number))
elif number < 0:
    print(f"{number} is negative")
else:
    print("number is zero")