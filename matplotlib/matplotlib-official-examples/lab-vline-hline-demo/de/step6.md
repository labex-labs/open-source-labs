# Horizontale Linien hinzufügen

In diesem Schritt werden wir horizontale Linien zum Graphen hinzufügen. Wir werden die `hlines`-Funktion von Matplotlib verwenden, um die horizontalen Linien zu zeichnen. Wir werden horizontale Linien bei y = 0,5, y = 2,5 und y = 4,5 zeichnen.

```python
# Add horizontal lines
hax.plot(s + nse, t, '^')
hax.hlines(t, [0], s, lw=2)
hax.set_xlabel('time (s)')
hax.set_title('Horizontal lines demo')
```
