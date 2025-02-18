# Verschieben der Tick-Labels der x-Achse nach oben

Um die Tick-Labels der x-Achse nach oben zu verschieben, verwenden wir die Funktion `tick_params()` und setzen die Parameter `top` und `labeltop` auf `True` sowie die Parameter `bottom` und `labelbottom` auf `False`.

```python
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
```
