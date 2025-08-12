import numpy as np

# MÉDIA ARITMÉTICA

media_aritmetica = np.mean(x)
print(media_aritmetica)

# DESVIO PADRÃO POPULACIONAL

desvio_populacional = np.std(x, ddof = 0)
print(desvio_populacional)

# DESVIO PADRÃO AMOSTRAL

desvio_amostral = np.std(x, ddof = 1)
print(desvio_amostral)

# VARIÂNCIA POPULACIONAL

variancia_populacional = np.var(x, ddof = 0)
print(variancia_populacional)

# VARIÂNCIA AMOSTRAL

variancia_amostral = np.var(x, ddof = 1)
print(variancia_amostral)

# MÉDIA PONDERADA

media_ponderada = np.average(x, weights = w)
print(media_ponderada)

# ERRO PADRÃO DA MÉDIA

incerteza_media = desvio_amostral / np.sqrt((len(x)))
print(incerteza_media)
