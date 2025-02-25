# Варианты семейства шрифтов

Первой характеристикой шрифта, которую мы рассмотрим, является вариант семейства шрифтов. Эта характеристика позволяет вам выбирать семейство шрифтов, используемое в вашем графике.

```python
# Show family options
fig.text(0.1, 0.9, 'family', fontproperties=heading_font, **alignment)
families = ['serif','sans-serif', 'cursive', 'fantasy','monospace']
for k, family in enumerate(families):
    font = FontProperties()
    font.set_family(family)
    fig.text(0.1, yp[k], family, fontproperties=font, **alignment)
```
