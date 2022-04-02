contadorLetras = lambda parametro: [len(i) for i in parametro]

soma = lambda a, b: a + b
multiplicacao = lambda a, b: a * b

if __name__ == '__main__':
    listaNome = ["Goku", "Saitama", "Seiya"]
    print(contadorLetras(listaNome))
    print(soma(20, 5))
    print(multiplicacao(5, 9))