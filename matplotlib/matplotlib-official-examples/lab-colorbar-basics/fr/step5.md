# Créer un tracé avec les données positives et négatives

Nous créons un tracé avec les données positives et négatives et ajoutons une barre de couleur au tracé en utilisant la fonction `colorbar`. Cette fois, nous spécifions les valeurs minimales et maximales pour la barre de couleur en utilisant les paramètres `vmin` et `vmax`.

```python
# Plot both positive and negative values between +/- 1.2
pos_neg_clipped = plt.imshow(Z, cmap='RdBu', vmin=-1.2, vmax=1.2,
                             interpolation='none')

# Add minorticks on the colorbar to make it easy to read the
# values off the colorbar.
cbar = plt.colorbar(pos_neg_clipped, extend='both')
cbar.minorticks_on()
```
