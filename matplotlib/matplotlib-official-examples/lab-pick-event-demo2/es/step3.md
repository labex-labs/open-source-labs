# Graficar los datos

Ahora, graficaremos mu vs. sigma usando el módulo `pyplot` de Matplotlib. Crearemos un diagrama de dispersión usando los valores calculados para mu y sigma. También agregaremos interactividad a la gráfica estableciendo el parámetro `picker` en True.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title('click on point to plot time series')
line, = ax.plot(xs, ys, 'o', picker=True, pickradius=5)
```
