# Graficar la superficie

En este paso, graficaremos la superficie utilizando la función `plot_surface()` de Matplotlib. Usaremos la paleta de colores `YlGnBu_r` para establecer el color de la superficie.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
```
