# Questão 1

import matplotlib.pyplot as plt
import numpy as np

P = [[2, 6, 8, 8, 12, 16, 20, 20, 22, 26], [58, 105, 88, 118, 117, 137, 158, 169, 149,202]]
eixo_x = P[0]
eixo_y = P[1]
plt.plot(eixo_x, eixo_y, 'mo')

soma_x = 0
soma_y = 0

for i in range(len(P[0])):
    soma_x += P[0][i]
    soma_y += P[1][i]

xm = soma_x / len(eixo_x)
ym = soma_y / len(eixo_y)

a1 = 0
a2 = 0
for i in range(len(P[1])):
    n = P[1][i] - ym
    m = P[0][i] - xm
    nm = n*m
    p = m**2
    a1 += nm
    a2 += p

a = float(a1/a2)
b = ym - a*xm
x = np.arange(0, 35, 1)
y = a*x + b

plt.plot(x, y)
plt.title("Gráfico da questão 1")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()