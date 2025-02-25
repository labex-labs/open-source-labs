# Hinzufügen von Ober- und Untergrenzen

Um sowohl Ober- als auch Untergrenzen zu den Fehlerbalken hinzuzufügen, werden wir sowohl das `uplims`- als auch das `lolims`-Parameter der `errorbar`-Funktion verwenden. Wir werden auch einen Marker zum Diagramm hinzufügen, um es von den vorherigen zu unterscheiden.

```python
# including upper and lower limits
ax.errorbar(x, y + 1.5, xerr=xerr, yerr=yerr, lolims=True, uplims=True,
            marker='o', markersize=8, linestyle='dotted')
```
