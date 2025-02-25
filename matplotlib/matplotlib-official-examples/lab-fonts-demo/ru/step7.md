# Жирный курсив

Последним параметром шрифта, который мы исследуем, является комбинация параметров стиля и толщины. Этот параметр позволяет вам выбирать стиль и толщину шрифта, используемые в вашем графике.

```python
# Show bold italic
font = FontProperties(style='italic', weight='bold', size='x-small')
fig.text(0.3, 0.1, 'bold italic', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='medium')
fig.text(0.3, 0.2, 'bold italic', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='x-large')
fig.text(0.3, 0.3, 'bold italic', fontproperties=font, **alignment)
```
