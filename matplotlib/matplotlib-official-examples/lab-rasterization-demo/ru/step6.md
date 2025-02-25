# Создаем график pcolormesh с наложенным текстом без растеризации

Мы создадим график pcolormesh с наложенным текстом без растеризации, чтобы показать, как векторные графические элементы могут сохранять свои преимущества для некоторых художников, таких как оси и текст.

```python
ax3.set_aspect(1)
ax3.pcolormesh(xx, yy, d)
ax3.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax3.transAxes)
ax3.set_title("No Rasterization")
```
