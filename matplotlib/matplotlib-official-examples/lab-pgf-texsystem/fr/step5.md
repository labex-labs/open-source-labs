# Ajuster la mise en page et enregistrer le graphique

Enfin, vous pouvez ajuster la mise en page de votre graphique et l'enregistrer dans un fichier à l'aide respectivement des fonctions `fig.tight_layout()` et `fig.savefig()`.

```python
fig.tight_layout(pad=.5)

fig.savefig("pgf_texsystem.pdf")
fig.savefig("pgf_texsystem.png")
```
