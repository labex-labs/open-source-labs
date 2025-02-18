# Рисование стрелок в конце осей координат (spines)

Для указания направления осей вы можете нарисовать стрелочки в конце осей координат (spines).

```python
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
```
