# Создаем график

Создадим простой линейный график с некоторыми длинными метками по оси y.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_yticks([2, 5, 7], labels=['really, really, really', 'long', 'labels'])
```
