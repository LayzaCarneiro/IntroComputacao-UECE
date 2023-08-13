# Questao 2

import matplotlib.pyplot as plt
import numpy as np

C1 = [[1, 3, 2, 4, 3, 2],[2, 4, 1, 3, 2, 2]]
C2 = [[7, 9, 8, 8, 9, 10],[9, 7, 8, 10, 7, 8]]
C1_eixo_x = C1[0]
C1_eixo_y = C1[1]
C2_eixo_x = C2[0]
C2_eixo_y = C2[1]
plt.plot(C1_eixo_x, C1_eixo_y, 'mo')
plt.plot(C2_eixo_x, C2_eixo_y, 'b^')

x1 = sum(C1[0]) / len(C1[0])
y1 = sum(C1[1]) / len(C1[1])
x2 = sum(C2[0]) / len(C2[0])
y2 = sum(C2[1]) / len(C2[1])
pm1 = [x1, x2]
pm2 = [y1, y2]
plt.plot(pm1, pm2)
plt.plot(pm1, pm2, 'rx')

SX = (x1 + x2)/2
SY = (y1 + y2)/2
a = -1/((y2 - y1)/(x2 - x1))
b = SY - a*SX
x = np.arange(0, 14, 1)
SM = a*x + b
plt.plot(x, SM)
plt.plot(SX, SY, 'ro')

plt.title("Gráfico da questão 1")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()