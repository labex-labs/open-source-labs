# Hinzufügen des Textfelds zum Diagramm

Schließlich werden wir das Textfeld mit `matplotlib.pyplot.text()` zum Diagramm hinzufügen. Wir werden die Position des Textfelds in Achsenkoordinaten angeben und den Parameter `bbox` verwenden, um die Eigenschaften des Felds hinzuzufügen.

```python
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
```
