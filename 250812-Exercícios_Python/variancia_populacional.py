x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
soma_quadrados = 0

for i in x:
  soma_quadrados = ((i - media_aritmetica) ** 2) + soma_quadrados

variancia_populacional = soma_quadrados / len(x)
print(variancia_populacional)
