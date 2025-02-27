# Die Proben plotten

Wir werden die Proben mit der `scatter`-Funktion aus `matplotlib.pyplot` plotten.

```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors="k")
```
