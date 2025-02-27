# Построение графика для выборки

Мы построим график для выборки с использованием функции `scatter` из `matplotlib.pyplot`.

```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors="k")
```
