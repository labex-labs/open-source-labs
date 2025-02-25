# Crear la gráfica

Crea un objeto de figura y eje utilizando `subplots`. Grafica los valores de x e y utilizando `plot`. Establece los límites del eje y para que empiecen en 0 utilizando `set_ylim`.

```python
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)
```
