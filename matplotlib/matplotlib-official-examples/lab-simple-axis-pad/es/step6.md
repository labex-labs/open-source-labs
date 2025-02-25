# Ajustar la posición de los valores de los ejes

En este paso, ajusta la posición de los valores de los ejes en el eje flotante. Esto se puede hacer estableciendo el atributo `tick_out` del objeto `major_ticks` en `True`.

```python
# Adjust Tick Position
fig = plt.figure(figsize=(9, 3.))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, wspace=0.01, hspace=0.01)

ax1 = setup_axes(fig, rect=121)
axis = add_floating_axis(ax1)

ax1 = setup_axes(fig, rect=122)
axis = add_floating_axis(ax1)
axis.major_ticks.set_tick_out(True)

plt.show()
```
