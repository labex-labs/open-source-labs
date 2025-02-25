# Definieren der Funktion für das Erstellen von Anmerkungskonnektionsstilen

Wir werden eine Funktion definieren, die zwei Parameter annimmt: das Achsenobjekt und den Verbindungsstil. Die Funktion wird zwei Datenpunkte plotten und eine Anmerkung mit dem angegebenen Verbindungsstil erstellen.

```python
def demo_con_style(ax, connectionstyle):
    x1, y1 = 0.3, 0.2
    x2, y2 = 0.8, 0.6

    ax.plot([x1, x2], [y1, y2], ".")
    ax.annotate("",
                xy=(x1, y1), xycoords='data',
                xytext=(x2, y2), textcoords='data',
                arrowprops=dict(arrowstyle="->", color="0.5",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle=connectionstyle,
                                ),
                )

    ax.text(.05,.95, connectionstyle.replace(",", ",\n"),
            transform=ax.transAxes, ha="left", va="top")
```
