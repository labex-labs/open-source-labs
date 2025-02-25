# Etiquetas de los ejes apuntando hacia afuera

En este paso, crearemos un subgráfico con las etiquetas de los ejes apuntando hacia afuera.

```python
fig = plt.figure(figsize=(6, 3))
fig.subplots_adjust(bottom=0.2)

ax = setup_axes(fig, 131)
for axis in ax.axis.values():
    axis.major_ticks.set_tick_out(True)
```
