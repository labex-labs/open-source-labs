# Erstellen der hatches_plot-Funktion

Die hatches_plot-Funktion wird ein Rechteck mit dem angegebenen Schraffierungsmuster erstellen und es zur Achse hinzufügen. Sie wird auch einen Text mit dem Schraffierungsmuster hinzufügen.

```python
def hatches_plot(ax, h):
    ax.add_patch(Rectangle((0, 0), 2, 2, fill=False, hatch=h))
    ax.text(1, -0.5, f"' {h} '", size=15, ha="center")
    ax.axis('equal')
    ax.axis('off')
```
