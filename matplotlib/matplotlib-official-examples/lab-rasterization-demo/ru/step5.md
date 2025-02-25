# Создаем график pcolormesh с растеризацией

Мы создадим график pcolormesh с растеризацией, чтобы показать, как растеризация может ускорить процесс рендеринга и создавать более мелкие файлы.

```python
ax2.set_aspect(1)
ax2.set_title("Rasterization")
ax2.pcolormesh(xx, yy, d, rasterized=True)
```
