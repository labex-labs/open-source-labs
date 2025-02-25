# Ajouter des lignes horizontales

Dans cette étape, nous allons ajouter des lignes horizontales au graphique. Nous utiliserons la fonction `hlines` de Matplotlib pour tracer les lignes horizontales. Nous tracerons des lignes horizontales à y = 0,5, y = 2,5 et y = 4,5.

```python
# Add horizontal lines
hax.plot(s + nse, t, '^')
hax.hlines(t, [0], s, lw=2)
hax.set_xlabel('time (s)')
hax.set_title('Horizontal lines demo')
```
