# Erstellen einer kontinuierlichen Norm

Wir werden eine kontinuierliche Norm erstellen, um von Datenpunkten zu Farben abzubilden. Wir werden die `Normalize`-Funktion aus `matplotlib.pyplot` verwenden, um die `dydx`-Werte zwischen ihrem Minimum und Maximum zu normalisieren. Anschließend werden wir die `LineCollection`-Funktion verwenden, um eine Reihe von Liniensegmenten zu erstellen und diese individuell nach ihrer Ableitung zu färben. Wir werden die `set_array`-Funktion verwenden, um die Werte festzulegen, die für die Farbzuordnung verwendet werden.

```python
norm = plt.Normalize(dydx.min(), dydx.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
