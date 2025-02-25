# Graficar la superficie

Finalmente, graficamos la superficie utilizando la función `plot_trisurf()`.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)
```
