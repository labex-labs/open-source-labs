# Personnalisez les sous-graphiques

Nous pouvons personnaliser les sous-graphiques selon les besoins. Par exemple, nous pouvons définir le titre de la figure à l'aide de la fonction `fig.suptitle()`, et nous pouvons formater les axes à l'aide de la fonction `format_axes()`.

```python
fig.suptitle("GridSpec")

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
