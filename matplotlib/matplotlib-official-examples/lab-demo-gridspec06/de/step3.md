# Figur und äußeres Gitter erstellen

Als nächstes werden wir die Figur und das äußere Gitter mit der Funktion `add_gridspec` erstellen. Wir werden ein 4x4-Gitter erstellen, wobei keine Leerraum zwischen den Teilplots vorhanden ist.

```python
fig = plt.figure(figsize=(8, 8))
outer_grid = fig.add_gridspec(4, 4, wspace=0, hspace=0)
```
