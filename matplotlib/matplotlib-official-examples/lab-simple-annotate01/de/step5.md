# Formanmerkung hinzufügen

Wir werden nun einer Formanmerkung zum Diagramm hinzufügen. Der folgende Code fügt ein Rechteck um den zweiten Datenpunkt hinzu.

```python
bbox = dict(boxstyle="round", fc="0.8")
ax.annotate("Data Point 2", xy=(2, 4), xytext=(2.5, 4.5),
            bbox=bbox,
            arrowprops=dict(facecolor="black", shrink=0.05))
```
