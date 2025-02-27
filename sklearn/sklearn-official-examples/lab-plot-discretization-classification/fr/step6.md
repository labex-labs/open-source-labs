# Visualiser les résultats

Dans cette étape, nous allons visualiser les résultats du processus de discrétisation des fonctionnalités. Nous allons tracer la précision de classification sur l'ensemble de test pour chaque classifieur et ensemble de données.

```python
plt.tight_layout()

# Ajouter des titres supérieurs au-dessus de la figure
plt.subplots_adjust(top=0.90)
suptitles = [
    "Classifieurs linéaires",
    "Discrétisation des fonctionnalités et classifieurs linéaires",
    "Classifieurs non-linéaires",
]
for i, suptitle in zip([1, 3, 5], suptitles):
    ax = axes[0, i]
    ax.text(
        1.05,
        1.25,
        suptitle,
        transform=ax.transAxes,
        horizontalalignment="center",
        size="x-large",
    )
plt.show()
```
