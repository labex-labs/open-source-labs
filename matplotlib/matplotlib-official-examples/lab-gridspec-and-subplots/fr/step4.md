# Supprimer les axes de base

Nous supprimons les axes de base qui sont recouverts par les axes plus grands que nous allons créer dans l'étape suivante.

```python
for ax in axs[1:, -1]:
    ax.remove()
```
