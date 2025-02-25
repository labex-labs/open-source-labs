# Показать размеры шрифтов

Наконец, мы покажем различные размеры шрифтов, доступные в Matplotlib. Мы будем использовать метод `fig.text()` для отображения каждого размера шрифта, где имя размера будет текстом, а соответствующий размер шрифта - в качестве именованного аргумента.

```python
fig.text(0.9, 0.9,'size', **alignment)
sizes = [
    'xx-small', 'x-small','small','medium', 'large', 'x-large', 'xx-large']
for k, size in enumerate(sizes):
    fig.text(0.9, yp[k], size, size=size, **alignment)
```
