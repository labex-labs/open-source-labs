# Закрашиваем области

Мы будем использовать `fill_between`, чтобы закрасить области выше и ниже горизонтальной линии, где синусоидальная волна положительна и отрицательна соответственно.

```python
ax.fill_between(t, 1, where=s > 0, facecolor='green', alpha=.5)
ax.fill_between(t, -1, where=s < 0, facecolor='red', alpha=.5)
```
