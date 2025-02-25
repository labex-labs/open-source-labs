# Стрелки масштабируются по ширине графика, а не по области просмотра

Функция `quiver()` может использоваться для создания графика векторных полей (quiver plot). По умолчанию стрелки на графике масштабируются в соответствии с данными, а не с самим графиком. Это может затруднять визуализацию стрелок, которые находятся близко к краям графика.

```python
import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(0, 2 * np.pi,.2), np.arange(0, 2 * np.pi,.2))
U = np.cos(X)
V = np.sin(Y)

fig1, ax1 = plt.subplots()
ax1.set_title('Arrows scale with plot width, not view')
Q = ax1.quiver(X, Y, U, V, units='width')
qk = ax1.quiverkey(Q, 0.9, 0.9, 2, r'$2 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
plt.show()
```
