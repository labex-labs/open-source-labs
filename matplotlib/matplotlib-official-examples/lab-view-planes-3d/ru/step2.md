# Определяем функцию для аннотации осей

Определяем функцию `annotate_axes`, которую мы будем использовать позже для присвоения меток каждому из основных трехмерных плоскостей обзора с соответствующими углами.

```python
def annotate_axes(ax, text, fontsize=18):
    ax.text(x=0.5, y=0.5, z=0.5, s=text,
            va="center", ha="center", fontsize=fontsize, color="black")
```
