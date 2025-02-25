# Configurer le style des axes

Nous allons maintenant configurer le style des axes en ajoutant des flèches à chaque extrémité des axes et en ajoutant les axes X et Y à partir de l'origine.

```python
for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")
    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)

# hides borders
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)
```
