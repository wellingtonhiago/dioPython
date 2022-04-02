
def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

print(soma(3, 4))
print(multiplicacao(5, 5))

print("-------------------------------------------")
class Calculadora:
    def __init__(self, num1, num2):
        self.valorA = num1
        self.valorB = num2

    def soma(a, b):
        return a + b

    def multiplicacao(a, b):
        return a * b

print(Calculadora.soma(3, 4))
print(Calculadora.multiplicacao(5, 5))

print("------------------------------------------")
class Calculadora:
    def __init__(self, num1, num2):
        self.valorA = num1
        self.valorB = num2

    def soma(self):
        return self.valorA + self.valorB

    def multiplicacao(self):
        return self.valorA * self.valorB

calculadora = Calculadora(10, 5)
print(calculadora.soma())
print(calculadora.multiplicacao())

print("------------------------------------------")
class Calculadora:

    def soma(self, valorA, valorB):
        return valorA + valorB

    def multiplicacao(self, valorA, valorB):
        return valorA * valorB

calculadora = Calculadora()
print(calculadora.soma(5, 6))
print(calculadora.multiplicacao(2, 3))