# Ajoutez du texte aux sous-graphiques

Nous allons ajouter du texte à chaque sous-graphique en utilisant la fonction `text`. Nous utiliserons les paramètres `rotation` (rotation), `horizontalalignment` (alignement horizontal), `verticalalignment` (alignement vertical) et `rotation_mode` (mode de rotation) pour faire tourner et aligner le texte. Nous utiliserons également le paramètre `bbox` (boîte englobante) pour souligner la boîte englobante du texte.

```python
kw = (
    {} if mode == "default" else
    {"bbox": dict(boxstyle="square,pad=0.", ec="none", fc="C1", alpha=0.3)}
)

texts = {}

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        tx = ax.text(0.5, 0.5, "Tpg",
                     size="x-large", rotation=40,
                     horizontalalignment=ha, verticalalignment=va,
                     rotation_mode=mode, **kw)
        texts[ax] = tx
```
