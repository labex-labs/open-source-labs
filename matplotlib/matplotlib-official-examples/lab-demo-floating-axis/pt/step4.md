# Criar os Eixos Host (Host Axes)

Nesta etapa, criaremos os eixos host e definiremos o auxiliar de grade. Usaremos `fig.add_subplot()` para criar os eixos host.

```python
# Create the host axes
fig = plt.figure(figsize=(5, 5))
ax1 = fig.add_subplot(axes_class=HostAxes, grid_helper=grid_helper)
```
