# Варианты размера

Пятым параметром шрифта, который мы исследуем, является вариант размера. Этот параметр позволяет вам выбирать размер шрифта, используемый в вашем графике.

```python
# Show size options
sizes = [
    'xx-small', 'x-small','small','medium', 'large', 'x-large', 'xx-large']
fig.text(0.9, 0.9,'size', fontproperties=heading_font, **alignment)
for k, size in enumerate(sizes):
    font = FontProperties()
    font.set_size(size)
    fig.text(0.9, yp[k], size, fontproperties=font, **alignment)
```
