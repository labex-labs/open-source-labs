# Masquer les axes inutiles

Vous souhaitez également masquer les axes supérieur et droit car ils ne sont pas nécessaires.

```python
ax.spines[["top", "right"]].set_visible(False)
```
