# Erstellen eines einfachen Pfeils

Jetzt werden wir einen einfachen ankergestützten Richtungspfeil mithilfe der Klasse `AnchoredDirectionArrows` erstellen. Dieser Pfeil wird die X- und Y-Richtungen im Graphen anzeigen.

```python
# Simple example
simple_arrow = AnchoredDirectionArrows(ax.transAxes, 'X', 'Y')
ax.add_artist(simple_arrow)
```
