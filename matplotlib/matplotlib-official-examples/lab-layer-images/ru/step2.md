# Определить переменные x и y

Определите переменные x и y для создания сеточной сетки (meshgrid).

```python
dx, dy = 0.05, 0.05
x = np.arange(-3.0, 3.0, dx)
y = np.arange(-3.0, 3.0, dy)
X, Y = np.meshgrid(x, y)
```
