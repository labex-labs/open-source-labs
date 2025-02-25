# Ein Gitternetz erstellen

Der dritte Schritt besteht darin, ein Gitternetz mit `linspace` zu erstellen.

```python
xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
```
