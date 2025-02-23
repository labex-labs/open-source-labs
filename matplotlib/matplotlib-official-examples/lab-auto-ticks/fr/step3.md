# Diagramme en points avec marge supplémentaire

Dans cette étape, nous allons définir une marge supplémentaire autour des données en utilisant `.Axes.set_xmargin` / `.Axes.set_ymargin` tout en respectant toujours le mode d'autolimitation avec des nombres arrondis.

```python
fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
ax.set_xmargin(0.8)
plt.show()
```
