# Criar um gráfico de oscilação amortecida e não amortecida

Primeiramente, criaremos uma figura com dois subplots, um para uma oscilação amortecida e outro para uma oscilação não amortecida. Usaremos a função `np.linspace()` para criar um array de valores de tempo e, em seguida, plotaremos os valores de amplitude correspondentes para cada tipo de oscilação usando as funções `np.cos()` e `np.exp()`.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 5.0, 501)

fig, (ax1, ax2) = plt.subplots(1, 2, layout='constrained', sharey=True)
ax1.plot(x, np.cos(6*x) * np.exp(-x))
ax1.set_title('damped')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('amplitude')

ax2.plot(x, np.cos(6*x))
ax2.set_xlabel('time (s)')
ax2.set_title('undamped')

fig.suptitle('Different types of oscillations', fontsize=16)

plt.show()
```
