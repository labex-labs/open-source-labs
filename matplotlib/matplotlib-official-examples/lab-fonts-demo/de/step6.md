# Größenoptionen

Die fünfte Schriftart-Eigenschaft, die wir untersuchen werden, ist die Größen-Option. Mit dieser Eigenschaft kannst du die Schriftgröße festlegen, die in deinem Diagramm verwendet wird.

```python
# Zeige Größenoptionen
sizes = [
    'xx-small', 'x-small','small','medium', 'large', 'x-large', 'xx-large']
fig.text(0.9, 0.9, 'größe', fontproperties=heading_font, **alignment)
for k, size in enumerate(sizes):
    font = FontProperties()
    font.set_size(size)
    fig.text(0.9, yp[k], size, fontproperties=font, **alignment)
```
