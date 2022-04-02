class Error(Exception):
    pass
class InputError(Error):
    def __init__(self, message):
        self.message = message
while True:
    try:
        i = int(input("Entre com um valor de 0 a 10: "))
        print(i)
        if i > 10:
            # raise Força a chamada de erro
            raise InputError("Nota não pode ser maior que 10")
        elif i < 0:
            raise InputError("Nota não pode ser menor que 0")
        break
    except  ValueError:
        print("Digite apenas números")
    except InputError as ex:
        print(ex)