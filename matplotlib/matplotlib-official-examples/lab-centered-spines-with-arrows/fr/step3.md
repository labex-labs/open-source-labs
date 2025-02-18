# Déplacement des axes (spines)

Par défaut, les axes (spines) sont dessinés aux bords du graphique. Dans ce cas, vous souhaitez déplacer les axes gauche et inférieur au centre du graphique.

```python
ax.spines[["left", "bottom"]].set_position(("data", 0))
```
