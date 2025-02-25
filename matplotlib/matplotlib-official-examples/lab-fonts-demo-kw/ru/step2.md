# Показать семейства шрифтов

Далее мы покажем различные семейства шрифтов, доступные в Matplotlib. Мы будем использовать метод `fig.text()` для отображения каждого семейства шрифтов, где имя семейства будет текстом, а соответствующее семейство шрифтов - в качестве именованного аргумента.

```python
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

fig.text(0.1, 0.9, 'family', size='large', **alignment)
families = ['serif','sans-serif', 'cursive', 'fantasy','monospace']
for k, family in enumerate(families):
    fig.text(0.1, yp[k], family, family=family, **alignment)
```
