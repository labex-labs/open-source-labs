# Rendre la ligne d'axe x visible à y = 0

Nous allons maintenant rendre la ligne d'axe x visible à y = 0. Cela se fait en rendant l'axe xzero visible.

```python
ax.axis["xzero"].set_visible(True)
ax.axis["xzero"].label.set_text("Axis Zero")
```
