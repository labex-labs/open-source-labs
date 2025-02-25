# Gewicht-Optionen

Die vierte Schriftart-Eigenschaft, die wir untersuchen werden, ist die Gewicht-Option. Mit dieser Eigenschaft kannst du das Schriftgewicht festlegen, das in deinem Diagramm verwendet wird.

```python
# Zeige Gewicht-Optionen
weights = ['light', 'normal','medium','semibold', 'bold', 'heavy', 'black']
fig.text(0.7, 0.9, 'weight', fontproperties=heading_font, **alignment)
for k, weight in enumerate(weights):
    font = FontProperties()
    font.set_weight(weight)
    fig.text(0.7, yp[k], weight, fontproperties=font, **alignment)
```
