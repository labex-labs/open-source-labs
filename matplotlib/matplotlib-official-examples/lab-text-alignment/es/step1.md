# Creando un rectángulo

Comenzaremos creando un rectángulo en el gráfico utilizando la función `Rectangle()` del módulo `matplotlib.patches`. Una vez creado el rectángulo, estableceremos sus límites horizontales y verticales utilizando las funciones `set_xlim()` y `set_ylim()`. Finalmente, agregaremos el rectángulo al gráfico.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

# Construye un rectángulo en coordenadas de ejes
left, width =.25,.5
bottom, height =.25,.5
right = left + width
top = bottom + height
p = Rectangle((left, bottom), width, height, fill=False)
ax.add_patch(p)

# Establece los límites horizontal y vertical
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
```
