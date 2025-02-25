# Crear una leyenda para líneas específicas

En este paso, crearemos una leyenda para líneas específicas.

```python
# Importar las bibliotecas necesarias
import matplotlib.pyplot as plt
import numpy as np

# Definir los datos para el gráfico
t1 = np.arange(0.0, 2.0, 0.1)
t2 = np.arange(0.0, 2.0, 0.01)

# Crear un gráfico con múltiples líneas
fig, ax = plt.subplots()
l1, = ax.plot(t2, np.exp(-t2))
l2, l3 = ax.plot(t2, np.sin(2 * np.pi * t2), '--o', t1, np.log(1 + t1), '.')
l4, = ax.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2),'s-.')

# Crear una leyenda para dos de las líneas
ax.legend((l2, l4), ('oscilatoria', 'amortiguada'), loc='upper right', shadow=True)

# Agregar etiquetas y título al gráfico
ax.set_xlabel('tiempo')
ax.set_ylabel('voltios')
ax.set_title('Oscilación amortiguada')

# Mostrar el gráfico
plt.show()
```
