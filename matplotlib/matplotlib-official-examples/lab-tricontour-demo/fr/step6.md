# Générer des motifs de hachures étiquetés sans couleur

Nous pouvons générer des motifs de hachures étiquetés sans couleur en spécifiant le paramètre `colors` comme `"none"` dans `ax.tricontourf`. Nous pouvons également créer une légende pour l'ensemble de lignes de niveau à l'aide de `ContourSet.legend_elements`.

```python
fig3, ax3 = plt.subplots()
n_levels = 7
tcf = ax3.tricontourf(
    triang,
    z,
    n_levels,
    colors="none",
    hatches=[".", "/", "\\", None, "\\\\", "*"],
)
ax3.tricontour(triang, z, n_levels, colors="black", linestyles="-")

artists, labels = tcf.legend_elements(str_format="{:2.1f}".format)
ax3.legend(artists, labels, handleheight=2, framealpha=1)
```
