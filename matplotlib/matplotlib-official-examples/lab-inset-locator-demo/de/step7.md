# Erstellen eines Einfügebereichs mit einer Begrenzungsbox als 2-Tupel

Wir können einen Einfügebereich mit einer Begrenzungsbox als 2-Tupel erstellen, indem wir die Breite und Höhe in Zoll angeben und den Parameter `bbox_to_anchor` verwenden, um die untere linke Ecke des Einfügebereichs anzugeben.

```python
# Erstellen Sie einen Einfügebereich mit einer Begrenzungsbox als 2-Tupel. Beachten Sie, dass dies eine
# Begrenzungsbox ohne Ausdehnung erstellt. Dies hat daher nur Sinn, wenn
# Breite und Höhe in absoluten Einheiten (Zoll) angegeben werden.
axins2 = inset_axes(ax, width=0.5, height=0.4,
                    bbox_to_anchor=(0.33, 0.25),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
```
