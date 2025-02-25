# Régler les limites et supprimer les graduations

Dans cette étape, nous allons régler la limite de l'axe des y et supprimer les graduations du graphique.

```python
# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 70)

# No ticks
ax.set_xticks([])
ax.set_yticks([])
```
