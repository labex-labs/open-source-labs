# Варианты стиля

Второй параметр шрифта, который мы исследуем, - это вариант стиля. Этот параметр позволяет вам выбирать стиль шрифта, используемый в вашем графике.

```python
# Show style options
styles = ['normal', 'italic', 'oblique']
fig.text(0.3, 0.9,'style', fontproperties=heading_font, **alignment)
for k, style in enumerate(styles):
    font = FontProperties()
    font.set_family('sans-serif')
    font.set_style(style)
    fig.text(0.3, yp[k], style, fontproperties=font, **alignment)
```
