# Ajuster le rembourrage de l'étiquette d'axe

Dans cette étape, ajustez le rembourrage de l'étiquette d'axe de l'axe flottant. Cela peut être fait en définissant l'attribut `pad` de l'objet `label` sur la valeur de rembourrage souhaitée.

```python
# Ajuster le rembourrage de l'étiquette d'axe
fig = plt.figure(figsize=(9, 3.))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, wspace=0.01, hspace=0.01)

ax1 = setup_axes(fig, rect=121)
axis = add_floating_axis(ax1)

ax1 = setup_axes(fig, rect=122)
axis = add_floating_axis(ax1)
axis.label.set_pad(20)

plt.show()
```
