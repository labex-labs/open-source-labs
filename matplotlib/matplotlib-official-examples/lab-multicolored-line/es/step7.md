# Crear un subgráfico

Crearemos un subgráfico para mostrar los segmentos de línea coloreados. Usaremos la función `subplots` de `matplotlib.pyplot` para crear una cuadrícula de subgráficos de 2x1, y los parámetros `sharex` y `sharey` para compartir los ejes x e y entre los subgráficos.

```python
fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
line = axs[0].add_collection(lc)
fig.colorbar(line, ax=axs[0])
```
