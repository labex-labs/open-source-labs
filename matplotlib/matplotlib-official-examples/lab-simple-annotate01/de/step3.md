# Text-Anmerkung hinzufügen

Wir werden nun einer Textanmerkung zum Diagramm hinzufügen. Der folgende Code fügt den Text "Data Point 1" an der ersten Datenposition hinzu.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05))
```
