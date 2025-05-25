# Definir uma função para anotar os eixos

Definimos uma função `annotate_axes` que usaremos mais tarde para rotular cada um dos planos de visualização 3D principais com seus respectivos ângulos.

```python
def annotate_axes(ax, text, fontsize=18):
    ax.text(x=0.5, y=0.5, z=0.5, s=text,
            va="center", ha="center", fontsize=fontsize, color="black")
```
