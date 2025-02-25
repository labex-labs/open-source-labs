# Показать варианты шрифтов

Далее мы покажем различные варианты шрифтов, доступные в Matplotlib. Мы будем использовать метод `fig.text()` для отображения каждого варианта шрифта, где имя варианта будет текстом, а соответствующий вариант шрифта - в качестве именованного аргумента.

```python
fig.text(0.5, 0.9, 'variant', **alignment)
variants = ['normal','small-caps']
for k, variant in enumerate(variants):
    fig.text(0.5, yp[k], variant, family='serif', variant=variant, **alignment)
```
