# Sous-échantillonnage de l'image avec interpolation 'nearest'

Maintenant, nous allons sous-échantillonner l'image de 450 pixels de données à 125 pixels ou 250 pixels en utilisant l'interpolation 'nearest'. Cela démontrera comment les données haute fréquence soumises au sous-échantillonnage peuvent causer des motifs de Moiré.

```python
fig, axs = plt.subplots(2, 2, figsize=(5, 6), layout='constrained')
axs[0, 0].imshow(a, interpolation='nearest', cmap='RdBu_r')
axs[0, 0].set_xlim(100, 200)
axs[0, 0].set_ylim(275, 175)
axs[0, 0].set_title('Zoom')

for ax, interp, space in zip(axs.flat[1:],
                             ['nearest', 'antialiased', 'antialiased'],
                             ['data', 'data', 'rgba']):
    ax.imshow(a, interpolation=interp, interpolation_stage=space,
              cmap='RdBu_r')
    ax.set_title(f"interpolation='{interp}'\nspace='{space}'")
plt.show()
```
