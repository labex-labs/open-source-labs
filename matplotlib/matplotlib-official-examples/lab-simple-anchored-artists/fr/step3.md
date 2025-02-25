# Ajouter des boîtes de texte

Ajoutez deux boîtes de texte à la figure, ancrées par des coins différents dans le coin supérieur gauche de la figure.

```python
at = AnchoredText("Figure 1a",
                  loc='upper left', prop=dict(size=8), frameon=True,
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at)

at2 = AnchoredText("Figure 1(b)",
                   loc='lower left', prop=dict(size=8), frameon=True,
                   bbox_to_anchor=(0., 1.),
                   bbox_transform=ax.transAxes
                   )
at2.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at2)
```
