# Ajouter des lignes verticales

Dans cette étape, nous allons ajouter des lignes verticales au graphique. Nous utiliserons la fonction `vlines` de Matplotlib pour tracer les lignes verticales. Nous utiliserons également le paramètre `transform` pour définir les coordonnées y à être mises à l'échelle de 0 à 1. Nous tracerons deux lignes verticales à x = 1 et x = 2.

```python
# Add vertical lines
vax.plot(t, s + nse, '^')
vax.vlines(t, [0], s)
vax.vlines([1, 2], 0, 1, transform=vax.get_xaxis_transform(), colors='r')
vax.set_xlabel('time (s)')
vax.set_title('Vertical lines demo')
```
