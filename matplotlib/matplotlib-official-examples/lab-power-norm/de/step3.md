# Daten erstellen

In diesem Schritt müssen Sie Daten mithilfe von `multivariate_normal()` erstellen. Diese Funktion generiert eine Zufallsstichprobe aus einer multivariate Normalverteilung.

```python
data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[3, 1], [1, 3]], size=1000)
])
```
