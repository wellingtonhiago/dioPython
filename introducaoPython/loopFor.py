for sequencia in range(10):
    print(sequencia) # 0 a 9

print("---------------------------")
for intervalo in range(30,40):
    print(intervalo) # 30 a 39

print("---------------------------")
# Imprime os números primos até 100
validarPrimo = int(input("Entre com um valor: "))
print("Esses valores são primos:")
for primo in range(validarPrimo + 1):
    div = 0
    for i in range(1, primo+1):
        resto = primo % i
        if resto == 0:
            div += 1
    if div == 2:
        print(primo)