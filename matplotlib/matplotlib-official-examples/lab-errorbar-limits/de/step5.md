# Hinzufügen von Untergrenzen

Um Untergrenzen zu den Fehlerbalken hinzuzufügen, werden wir das `lolims`-Parameter der `errorbar`-Funktion verwenden. Wir werden auch einen konstanten Wert von 1,0 zu den y-Werten hinzufügen, um dieses Diagramm von den vorherigen zu unterscheiden.

```python
# including lower limits
ax.errorbar(x, y + 1.0, xerr=xerr, yerr=yerr, lolims=True, linestyle='dotted')
```
