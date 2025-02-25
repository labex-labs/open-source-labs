# Création de sous-graphiques avec mise en page contraignante

Nous créons les mêmes sous-graphiques 2x2, mais cette fois-ci nous utilisons la mise en page contraignante (_constrained layout_). Cela ajuste automatiquement les sous-graphiques pour empêcher les chevauchements entre les objets d'axes et les étiquettes.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')

for ax in axs.flat:
    example_plot(ax)
```
