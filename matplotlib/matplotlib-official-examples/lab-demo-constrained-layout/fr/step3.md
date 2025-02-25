# Création de sous-graphiques sans mise en page contraignante

Nous créons une figure avec des sous-graphiques 2x2 sans utiliser la fonction _constrained layout_. Cela entraîne des chevauchements d'étiquettes sur les axes.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout=None)

for ax in axs.flat:
    example_plot(ax)
```
