# Plotar a Superfície

Nesta etapa, plotaremos a superfície usando a função `plot_surface()` do Matplotlib. Usaremos o mapa de cores `YlGnBu_r` para definir a cor da superfície.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
```
