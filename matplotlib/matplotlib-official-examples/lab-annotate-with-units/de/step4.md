# Hinzufügen einer Pfeilanmerkung mit unitisierten xy- und Textwerten

In diesem Schritt fügen wir eine Pfeilanmerkung zum Diagramm hinzu, indem wir die Funktion `annotate()` verwenden. Wir geben die Position der Pfeile, den anzuzeigenden Text und die Pfeileigenschaften an. Wir werden auch die Maßeinheiten für die Position und den Text angeben.

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8*cm, 0.95*cm), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
