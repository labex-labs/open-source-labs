# Définir les titres et les étiquettes

Nous allons définir les titres et les étiquettes pour les sous-graphiques.

```python
    if i == 0:
        axes_row[0].set_title("Pénalité L1")
        axes_row[1].set_title("Elastic-Net\nl1_ratio = %s" % l1_ratio)
        axes_row[2].set_title("Pénalité L2")

    axes_row[0].set_ylabel("C = %s" % C)
```
