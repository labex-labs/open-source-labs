# Ajustar a Posição das Marcas de Escala (Ticks)

Nesta etapa, ajuste a posição das marcas de escala (ticks) no eixo flutuante. Isso pode ser feito definindo o atributo `tick_out` do objeto `major_ticks` para `True`.

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
