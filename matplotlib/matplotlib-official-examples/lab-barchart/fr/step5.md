# Personnaliser le graphique

Nous pouvons personnaliser le graphique en ajoutant des étiquettes, un titre et en ajustant les étiquettes d'échelonnement de l'axe x et la légende. Nous allons également définir la limite de l'axe y pour vous assurer que toutes nos données sont visibles.

```python
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)
```
