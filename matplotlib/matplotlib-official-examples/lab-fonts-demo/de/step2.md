# Schriftfamilieoptionen

Die erste Schriftart-Eigenschaft, die wir untersuchen werden, ist die Schriftfamilie-Option. Mit dieser Eigenschaft kannst du die Schriftfamilie festlegen, die in deinem Diagramm verwendet wird.

```python
# Zeige Schriftfamilie-Optionen
fig.text(0.1, 0.9, 'family', fontproperties=heading_font, **alignment)
families = ['serif','sans-serif', 'cursive', 'fantasy','monospace']
for k, family in enumerate(families):
    font = FontProperties()
    font.set_family(family)
    fig.text(0.1, yp[k], family, fontproperties=font, **alignment)
```
