# Crear un gráfico de línea simple

Comencemos creando un gráfico de línea simple. En este ejemplo, graficaremos las funciones seno y coseno en el intervalo [0, 2π].

```python
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin')
plt.plot(x, y2, label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.show()
```
