# Создаем график pcolormesh с наложенным текстом с растеризацией

Мы создадим график pcolormesh с наложенным текстом с растеризацией, чтобы показать, как растеризация позволяет векторным графическим элементам сохранять свои преимущества для некоторых художников, таких как оси и текст.

```python
ax4.set_aspect(1)
m = ax4.pcolormesh(xx, yy, d, zorder=-10)
ax4.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax4.transAxes)
ax4.set_rasterization_zorder(0)
ax4.set_title("Rasterization z$<-10$")
```
