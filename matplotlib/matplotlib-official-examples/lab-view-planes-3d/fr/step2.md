# Définissez une fonction pour annoter les axes

Nous définissons une fonction `annotate_axes` que nous utiliserons plus tard pour étiqueter chacun des plans de vue principaux 3D avec leurs angles respectifs.

```python
def annotate_axes(ax, text, fontsize=18):
    ax.text(x=0.5, y=0.5, z=0.5, s=text,
            va="center", ha="center", fontsize=fontsize, color="black")
```
