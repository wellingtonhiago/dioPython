lista = [1,10]
try:
    divisão = 10/1
    numero = lista[3]
except ZeroDivisionError:
    print("Erro ao dividir por zero")
except IndexError:
    print("Erro ao acessar índice inexistente")
# BasseException é uma classe pai
except BaseException as ex:
    print("Erro desconhecido. Erro: {}".format(ex))
else:
    print("Executa quando não ocorre exceção")
finally:
    print("Sempre executa")