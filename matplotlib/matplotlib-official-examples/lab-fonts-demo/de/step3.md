# Stiloptionen

Die zweite Schriftart-Eigenschaft, die wir untersuchen werden, ist die Stil-Option. Mit dieser Eigenschaft kannst du den Schriftstil festlegen, der in deinem Diagramm verwendet wird.

```python
# Zeige Stiloptionen
styles = ['normal', 'italic', 'oblique']
fig.text(0.3, 0.9,'style', fontproperties=heading_font, **alignment)
for k, style in enumerate(styles):
    font = FontProperties()
    font.set_family('sans-serif')
    font.set_style(style)
    fig.text(0.3, yp[k], style, fontproperties=font, **alignment)
```
