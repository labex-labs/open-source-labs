# Alinear manualmente las etiquetas y

El cuarto paso es alinear manualmente las etiquetas y utilizando el método `~.Axis.set_label_coords` del objeto del eje y.

```python
fig, axs = plt.subplots(2, 2)
fig.subplots_adjust(left=0.2, wspace=0.6)
make_plot(axs)

labex = -0.3  # coordenadas de los ejes

for j in range(2):
    axs[j, 1].yaxis.set_label_coords(labex, 0.5)

plt.show()
```
