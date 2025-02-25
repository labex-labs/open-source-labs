# Definir una función para anotar los ejes

Definimos una función `annotate_axes` que usaremos más adelante para etiquetar cada uno de los planos principales de vista tridimensional con sus respectivos ángulos.

```python
def annotate_axes(ax, text, fontsize=18):
    ax.text(x=0.5, y=0.5, z=0.5, s=text,
            va="center", ha="center", fontsize=fontsize, color="black")
```
