listaNumero = [1, 2, 3, 4]
listaAnimal = ["Gato", "Cachorro", "Leão"]

print(listaNumero)

print("----------------------")
print(sum(listaNumero))

print("----------------------")
print(max(listaNumero))
print(min(listaNumero))

print("----------------------")
print(listaAnimal)

print("----------------------")
print(listaAnimal[2])

print("----------------------")
print(max(listaAnimal))
print(min(listaAnimal))

print("----------------------")
for i in listaAnimal:
    print(i)

print("----------------------")
if "Lobo" in listaAnimal:
    print("Existe lobo")
else:
    print("Não existe lobo, ele será incluido")
    listaAnimal.append("Lobo")
    print(listaAnimal)

print("----------------------")
listaAnimal2 = listaAnimal * 2
listaNumero2 = listaNumero * 2
print(listaAnimal2)
print(listaNumero2)

print("----------------------")
# Retira o último da lista
listaAnimal.pop()
# Retira o número 0 da lista
listaAnimal.pop(0)
# Remove com o nome
listaAnimal2.remove("Cachorro")

print("----------------------")
# Ordenando a lista
listaAnimal2.sort()
print(listaAnimal2)

# Ordenar de forma reversa
listaAnimal2.reverse()
print(listaAnimal2)

# Convertendo lista em tupla
listaAnimal = tuple(listaAnimal)
# Convertendo tupla em lista
listaAnimal = list(listaAnimal)