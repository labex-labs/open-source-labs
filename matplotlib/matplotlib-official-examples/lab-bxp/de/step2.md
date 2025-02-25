# Boxplot-Statistiken berechnen

Die `boxplot_stats()`-Funktion aus dem `matplotlib.cbook`-Modul berechnet die für das Boxplot-Diagramm erforderlichen Statistiken. Wir übergeben die Daten und die Bezeichnungen als Parameter.

```python
# Compute boxplot stats
stats = cbook.boxplot_stats(data, labels=labels, bootstrap=10000)
```
