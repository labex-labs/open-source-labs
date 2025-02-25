# Vertikale Linien hinzufügen

In diesem Schritt werden wir vertikale Linien zum Graphen hinzufügen. Wir werden die `vlines`-Funktion von Matplotlib verwenden, um die vertikalen Linien zu zeichnen. Wir werden auch den `transform`-Parameter verwenden, um die y-Koordinaten so zu skalieren, dass sie von 0 bis 1 reichen. Wir werden zwei vertikale Linien bei x = 1 und x = 2 zeichnen.

```python
# Add vertical lines
vax.plot(t, s + nse, '^')
vax.vlines(t, [0], s)
vax.vlines([1, 2], 0, 1, transform=vax.get_xaxis_transform(), colors='r')
vax.set_xlabel('time (s)')
vax.set_title('Vertical lines demo')
```
