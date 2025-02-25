# Hinzufügen von Obergrenzen

Um Obergrenzen zu den Fehlerbalken hinzuzufügen, werden wir das `uplims`-Parameter der `errorbar`-Funktion verwenden. Wir werden auch einen konstanten Wert von 0,5 zu den y-Werten hinzufügen, um dieses Diagramm von dem vorherigen zu unterscheiden.

```python
# including upper limits
ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=True, linestyle='dotted')
```
