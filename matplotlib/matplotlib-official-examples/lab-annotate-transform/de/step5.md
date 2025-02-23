# Anmerkungen hinzufügen

Der letzte Schritt besteht darin, Anmerkungen zum Diagramm hinzuzufügen. Wir werden die Methode `ax.annotate` verwenden, um Text und Pfeile zum Diagramm hinzuzufügen. Wir werden auch die Parameter `bbox` und `arrowprops` verwenden, um die Anmerkungen zu gestalten.

```python
bbox = dict(boxstyle="round", fc="0.8")
arrowprops = dict(
    arrowstyle="->",
    connectionstyle="angle,angleA=0,angleB=90,rad=10")

offset = 72
ax.annotate(
    f'data = ({xdata:.1f}, {ydata:.1f})',
    (xdata, ydata),
    xytext=(-2*offset, offset), textcoords='offset points',
    bbox=bbox, arrowprops=arrowprops)
ax.annotate(
    f'display = ({xdisplay:.1f}, {ydisplay:.1f})',
    xy=(xdisplay, ydisplay), xycoords='figure pixels',
    xytext=(0.5*offset, -offset), textcoords='offset points',
    bbox=bbox, arrowprops=arrowprops)
```
