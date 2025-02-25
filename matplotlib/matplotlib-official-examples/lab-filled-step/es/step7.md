# Crear el histograma con sombreado

Crearemos un histograma con sombreado utilizando la función `stack_hist` que definimos anteriormente. Utilizaremos los `stack_data`, `color_cycle` y `hist_func` que definimos anteriormente. También estableceremos `plot_kwargs` para incluir el color del borde y la orientación.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)
arts = stack_hist(ax1, stack_data, color_cycle + label_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, stack_data, color_cycle, hist_func=hist_func, plot_kwargs=dict(edgecolor='w', orientation='h'))
ax1.set_ylabel('conteos')
ax1.set_xlabel('x')
ax2.set_xlabel('conteos')
ax2.set_ylabel('x')
```
