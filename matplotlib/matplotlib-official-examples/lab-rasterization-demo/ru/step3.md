# Создаем фигуру с четырьмя подграфиками

Мы создадим фигуру с четырьмя подграфиками, чтобы проиллюстрировать разные аспекты растеризации.

```python
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, layout="constrained")
```
