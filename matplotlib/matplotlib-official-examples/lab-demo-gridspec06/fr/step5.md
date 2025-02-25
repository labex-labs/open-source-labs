# Afficher seulement les bords externes

Dans cette étape, nous allons supprimer les bords des sous-graphiques intérieurs et n'afficher que les bords externes. Cela rendra le tracé plus propre.

```python
for ax in fig.get_axes():
    ss = ax.get_subplotspec()
    ax.spines.top.set_visible(ss.is_first_row())
    ax.spines.bottom.set_visible(ss.is_last_row())
    ax.spines.left.set_visible(ss.is_first_col())
    ax.spines.right.set_visible(ss.is_last_col())
```
