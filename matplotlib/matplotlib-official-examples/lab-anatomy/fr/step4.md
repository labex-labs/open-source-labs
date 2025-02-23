# Ajouter des étiquettes et un titre

Nous allons maintenant ajouter des étiquettes aux axes x et y, et un titre à la figure en utilisant les méthodes `set_xlabel()`, `set_ylabel()` et `set_title()`.

```python
# Ajouter des étiquettes et un titre
ax.set_xlabel("x Axis label", fontsize=14)
ax.set_ylabel("y Axis label", fontsize=14)
ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment='bottom')
```
