# Создаем график pcolormesh без растеризации

Мы создадим график pcolormesh без растеризации, чтобы проиллюстрировать разницу между растеризацией и отсутствием растеризации.

```python
ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.set_title("No Rasterization")
```
