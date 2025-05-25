# Criar uma Meshgrid

O terceiro passo é criar uma meshgrid usando `linspace`.

```python
xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
```
