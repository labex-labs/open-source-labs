# Показать веса шрифтов

Теперь мы покажем различные веса шрифтов, доступные в Matplotlib. Мы будем использовать метод `fig.text()` для отображения каждого веса шрифта, где имя веса будет текстом, а соответствующий вес шрифта - в качестве именованного аргумента.

```python
fig.text(0.7, 0.9, 'weight', **alignment)
weights = ['light', 'normal','medium','semibold', 'bold', 'heavy', 'black']
for k, weight in enumerate(weights):
    fig.text(0.7, yp[k], weight, weight=weight, **alignment)
```
