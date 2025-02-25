# Делаем ось x видимой при y = 0

Теперь сделаем ось x видимой при y = 0. Это достигается путем настройки оси xzero на видимость.

```python
ax.axis["xzero"].set_visible(True)
ax.axis["xzero"].label.set_text("Axis Zero")
```
