# Étiquettes d'échelle pointant vers l'extérieur

Dans cette étape, nous allons créer un sous-graphique avec des étiquettes d'échelle pointant vers l'extérieur.

```python
fig = plt.figure(figsize=(6, 3))
fig.subplots_adjust(bottom=0.2)

ax = setup_axes(fig, 131)
for axis in ax.axis.values():
    axis.major_ticks.set_tick_out(True)
```
