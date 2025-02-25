# Créer des insets avec des positions arbitraires

Nous pouvons créer des insets avec des positions arbitraires en utilisant le paramètre `bbox_to_anchor` pour spécifier une boîte englobante en coordonnées de données et en utilisant le paramètre `bbox_transform` pour spécifier la transformation de la boîte englobante.

```python
# Crée un inset en coordonnées de données en utilisant ax.transData comme transformation
axins3 = inset_axes(ax2, width="100%", height="100%",
                    bbox_to_anchor=(1e-2, 2, 1e3, 3),
                    bbox_transform=ax2.transData, loc=2, borderpad=0)
```
