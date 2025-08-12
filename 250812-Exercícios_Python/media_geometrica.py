x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
produto_total = 1

for i in x:
  produto_total = produto_total * i

media_geometrica = produto_total ** (1 / len(x))
print(media_geometrica)
