# Définissez les limites et les étiquettes du graphique

Nous allons définir les limites et les étiquettes du graphique pour correspondre à la sortie souhaitée.

```python
for ax in axs:
    ax.set(xlim=(-0.1, 1.1), ylim=(-.8, 3.9), xticks=[], yticks=[])
    ax.set_title(f"usetex={ax.usetex}\n")
```
