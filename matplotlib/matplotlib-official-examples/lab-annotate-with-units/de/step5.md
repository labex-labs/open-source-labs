# Hinzufügen einer Pfeilanmerkung mit gemischten Maßeinheiten

In diesem Schritt fügen wir eine weitere Pfeilanmerkung zum Diagramm hinzu, indem wir die Funktion `annotate()` verwenden. Wir geben die Position der Pfeile, den anzuzeigenden Text und die Pfeileigenschaften an. Wir werden auch Maßeinheiten für die Position mischen und die Achsenbrüche für den Text verwenden.

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
