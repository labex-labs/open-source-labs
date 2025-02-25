# Ajouter des lignes de grille et des étiquettes

Nous allons ajouter des lignes de grille horizontales, définir les étiquettes de l'axe x et de l'axe y aux graphiques.

```python
for ax in axs:
    ax.yaxis.grid(True)
    ax.set_xticks([y + 1 for y in range(len(all_data))], labels=['x1', 'x2', 'x3', 'x4'])
    ax.set_xlabel('Four separate samples')
    ax.set_ylabel('Observed values')
```
