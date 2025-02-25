# Crear una nueva Figura y Ejes

El primer paso es crear una nueva figura y un eje que la llene. Esta será la superficie en la que se dibujará la simulación.

```python
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
```
