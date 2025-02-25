# Создать сетку

Третий шаг - создать сетку с использованием `linspace`.

```python
xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
```
