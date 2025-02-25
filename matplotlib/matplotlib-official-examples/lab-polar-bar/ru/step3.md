# Определяем данные

Мы определим данные для диаграммы. Мы сгенерируем 20 случайных значений для радиусов и углов.

```python
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
colors = plt.cm.viridis(radii / 10.)
```
