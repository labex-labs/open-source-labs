# Graficado con márgenes

El método `margins()` en Matplotlib se puede utilizar para establecer márgenes en la gráfica en lugar de utilizar los métodos `set_xlim()` y `set_ylim()`. En este paso, aprenderemos a hacer zoom in y out en una gráfica utilizando el método `margins()` en lugar de los métodos `set_xlim()` y `set_ylim()`.

```python
import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 3.0, 0.01)

# crea un subgráfico con márgenes
ax1 = plt.subplot(212)
ax1.margins(0.05) # el margen predeterminado es 0.05, el valor 0 significa ajustar
ax1.plot(t1, f(t1))

# crea un subgráfico con márgenes ampliados
ax2 = plt.subplot(221)
ax2.margins(2, 2) # valores >0.0 amplían
ax2.plot(t1, f(t1))
ax2.set_title('Ampliado')

# crea un subgráfico con márgenes reducidos
ax3 = plt.subplot(222)
ax3.margins(x=0, y=-0.25) # valores en (-0.5, 0.0) se acercan al centro
ax3.plot(t1, f(t1))
ax3.set_title('Reducido')

plt.show()
```
