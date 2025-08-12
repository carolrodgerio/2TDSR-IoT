x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
soma_inversa = 0

# inverso = n ^ -1 = 1 / n

for i in x:
  soma_inversa = (1 / i) + soma_inversa

media_harmonica = len(x) / soma_inversa
print(media_harmonica)
