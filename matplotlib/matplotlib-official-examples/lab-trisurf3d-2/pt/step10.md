# Plotar a Superfície

Finalmente, plotamos a superfície usando a função `plot_trisurf()`.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)
```
