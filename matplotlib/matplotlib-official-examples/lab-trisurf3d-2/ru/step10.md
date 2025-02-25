# Построение поверхности

Наконец, мы строим поверхность с использованием функции `plot_trisurf()`.

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)
```
