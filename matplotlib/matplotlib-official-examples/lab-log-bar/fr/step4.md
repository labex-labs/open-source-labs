# Personnalisation du graphique

Nous pouvons personnaliser l'apparence de notre graphique en ajoutant des étiquettes à l'axe x et à l'axe y, et en définissant l'échelle de l'axe y en logarithme.

```python
ax.set_xticks(x + dimw / 2, labels=map(str, x))
ax.set_yscale('log')

ax.set_xlabel('x')
ax.set_ylabel('y')
```
