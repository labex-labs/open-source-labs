# Erstellen des 3D-Stammdiagramms

In diesem Schritt erstellen wir das 3D-Stammdiagramm mithilfe der `stem`-Funktion aus Matplotlib. Wir übergeben die x-, y- und z-Koordinaten als Argumente an die `stem`-Funktion.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

plt.show()
```
