# Création de grille de sous-graphiques imbriquées avec mise en page contraignante

Nous créons un exemple plus complexe en utilisant des grille de sous-graphiques imbriquées avec la mise en page contraignante (_constrained layout_). Cela nous permet d'avoir plus de contrôle sur la disposition des sous-graphiques.

```python
fig = plt.figure(layout='constrained')

gs0 = gridspec.GridSpec(1, 2, figure=fig)

gs1 = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=gs0[0])
for n in range(3):
    ax = fig.add_subplot(gs1[n])
    example_plot(ax)


gs2 = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs0[1])
for n in range(2):
    ax = fig.add_subplot(gs2[n])
    example_plot(ax)

plt.show()
```
