# Spines für die untere und linke Seite anpassen

Im zweiten Subplot werden wir Spines nur auf der unteren und linken Seite des Graphen anzeigen. Wir können die Spines auf der rechten und oberen Seite des Graphen mit der `set_visible`-Methode ausblenden.

```python
ax1.plot(x, y)
ax1.set_title('Bottom-Left Spines')

# Hide the right and top spines
ax1.spines.right.set_visible(False)
ax1.spines.top.set_visible(False)
```
