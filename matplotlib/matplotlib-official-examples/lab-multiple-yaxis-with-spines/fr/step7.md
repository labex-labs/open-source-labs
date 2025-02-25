# Réglez les couleurs des graduations

Nous réglons les couleurs des graduations pour chaque axe y pour qu'elles correspondent à la couleur des étiquettes.

```python
ax.tick_params(axis='y', colors=p1.get_color())
twin1.tick_params(axis='y', colors=p2.get_color())
twin2.tick_params(axis='y', colors=p3.get_color())
```
