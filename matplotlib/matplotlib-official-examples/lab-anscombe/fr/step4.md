# Tracer les données

Pour chaque sous-graphique, nous allons tracer les points de données x et y et ajouter une ligne de régression linéaire. Nous ajouterons également une boîte de texte avec quelques statistiques sur les données.

```python
datasets = {
    'I': (x, y1),
    'II': (x, y2),
    'III': (x, y3),
    'IV': (x4, y4)
}

for ax, (label, (x, y)) in zip(axs.flat, datasets.items()):
    ax.text(0.1, 0.9, label, fontsize=20, transform=ax.transAxes, va='top')
    ax.tick_params(direction='in', top=True, right=True)
    ax.plot(x, y, 'o')

    # régression linéaire
    p1, p0 = np.polyfit(x, y, deg=1)  # pente, ordonnée à l'origine
    ax.axline(xy1=(0, p0), slope=p1, color='r', lw=2)

    # ajouter une boîte de texte pour les statistiques
    stats = (f'$\\mu$ = {np.mean(y):.2f}\n'
             f'$\\sigma$ = {np.std(y):.2f}\n'
             f'$r$ = {np.corrcoef(x, y)[0][1]:.2f}')
    bbox = dict(boxstyle='round', fc='blanchedalmond', ec='orange', alpha=0.5)
    ax.text(0.95, 0.07, stats, fontsize=9, bbox=bbox,
            transform=ax.transAxes, horizontalalignment='right')

plt.show()
```
