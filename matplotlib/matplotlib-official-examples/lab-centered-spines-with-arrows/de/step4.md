# Verstecken unnötiger Achsenlinien (Spines)

Sie möchten auch die oberen und rechten Achsenlinien (Spines) verstecken, da sie nicht benötigt werden.

```python
ax.spines[["top", "right"]].set_visible(False)
```
