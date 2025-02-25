# Crear una figura con dos ejes

En este paso, creamos una figura con dos ejes. Usamos el método `add_axes` para agregar dos ejes a la figura. También establecemos la etiqueta de la marca en el eje y para el primer eje y el título para el segundo eje.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 0.5])
ax2 = fig.add_axes([0, 0.5, 1, 0.5])

ax1.set_yticks([0.5], labels=["very long label"])
ax1.set_ylabel("Y label")

ax2.set_title("Title")
```
