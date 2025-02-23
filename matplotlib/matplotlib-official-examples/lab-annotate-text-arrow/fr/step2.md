# Ajout d'annotations de texte au graphique

Ensuite, nous ajouterons des annotations de texte au graphique en utilisant la fonction `ax.text()`. Nous créerons deux annotations, l'une pour "Échantillon A" et l'autre pour "Échantillon B".

```python
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.text(-2, -2, "Sample A", ha="center", va="center", size=20,
        bbox=bbox_props)
ax.text(2, 2, "Sample B", ha="center", va="center", size=20,
        bbox=bbox_props)
```
