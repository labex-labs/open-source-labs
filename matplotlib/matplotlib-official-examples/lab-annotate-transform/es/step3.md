# Crear el gráfico

Ahora, crearemos el gráfico usando la biblioteca `matplotlib.pyplot`. Estableceremos los límites de los ejes x e y y luego graficaremos los datos.

```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
```
