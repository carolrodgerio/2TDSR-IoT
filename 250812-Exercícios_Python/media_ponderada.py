x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
w = [113, 88, 58, 65, 71, 46, 36, 33, 37, 40, 24, 21, 20, 15, 20]

lista_ponderada = [a * b for a, b in zip(x, w)]
media_ponderada = sum(lista_ponderada) / sum(w)
print(media_ponderada)
