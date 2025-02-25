# Hinzufügen von Teilgrafiken zu GridSpec

Wir können Teilgrafiken zu GridSpec hinzufügen, indem wir die Funktion `fig.add_subplot()` verwenden. Wir können die Position der Teilgrafik im Gitter mithilfe der Indexnotation des GridSpec-Objekts angeben. Beispielsweise gibt `gs[0, :]` die erste Zeile und alle Spalten an.

```python
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])
```
