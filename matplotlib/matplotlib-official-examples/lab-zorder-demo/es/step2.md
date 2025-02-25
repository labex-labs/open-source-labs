# Cambiando zorder

Para cambiar el orden de dibujo de los artistas, podemos establecer su atributo `zorder` explícitamente utilizando el parámetro `zorder` al crear el artista. Por ejemplo, podemos mover los puntos encima de las líneas en un diagrama de dispersión estableciendo el `zorder` de los puntos en un valor mayor que el `zorder` de la línea.

```python
import matplotlib.pyplot as plt
import numpy as np

r = np.linspace(0.3, 1, 30)
theta = np.linspace(0, 4*np.pi, 30)
x = r * np.sin(theta)
y = r * np.cos(theta)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3.2))

ax1.plot(x, y, 'C3', lw=3)
ax1.scatter(x, y, s=120)
ax1.set_title('Lines on top of dots')

ax2.plot(x, y, 'C3', lw=3)
ax2.scatter(x, y, s=120, zorder=2.5)  # move dots on top of line
ax2.set_title('Dots on top of lines')

plt.tight_layout()
plt.show()
```
