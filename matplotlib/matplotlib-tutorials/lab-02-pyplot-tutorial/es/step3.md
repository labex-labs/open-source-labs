# Graficando múltiples líneas

También podemos graficar múltiples líneas con diferentes estilos en una llamada a la función utilizando arrays. Grafiquemos tres líneas: una línea roja discontinua, cuadrados azules y triángulos verdes:

```python
import numpy as np

t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

Explicación:

- Utilizamos el módulo `numpy` para crear un array `t` con valores de tiempo muestreados uniformemente.
- La función `plot` se llama con tres pares de valores `x` e `y`, seguidos de las cadenas de formato `'r--'` (línea roja discontinua), `'bs'` (cuadrados azules) y `'g^'` (triángulos verdes).
