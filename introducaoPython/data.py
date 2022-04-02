from datetime import date


dataAtual = date.today()
dataAtualStr = dataAtual.strftime("%A/%B/%Y")
print(dataAtualStr)