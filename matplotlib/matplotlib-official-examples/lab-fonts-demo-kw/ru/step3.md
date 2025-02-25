# Показать стили шрифта

Теперь мы покажем различные стили шрифта, доступные в Matplotlib. Мы будем использовать метод `fig.text()` для отображения каждого стиля шрифта, где имя стиля будет текстом, а соответствующий стиль шрифта - в качестве именованного аргумента.

```python
fig.text(0.3, 0.9,'style', **alignment)
styles = ['normal', 'italic', 'oblique']
for k, style in enumerate(styles):
    fig.text(0.3, yp[k], style, family='sans-serif', style=style, **alignment)
```
