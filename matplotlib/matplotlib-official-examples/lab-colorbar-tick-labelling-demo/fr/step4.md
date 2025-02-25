# Créez un graphique avec une barre de couleur horizontale

Nous allons maintenant créer un graphique avec une barre de couleur horizontale. Nous allons suivre les mêmes étapes que dans l'Étape 2, mais cette fois-ci nous utiliserons la carte de couleur `afmhot` et définirons l'orientation de la barre de couleur sur horizontale.

```python
# Make plot with horizontal colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.afmhot)
ax.set_title('Gaussian noise with horizontal colorbar')

cbar = fig.colorbar(cax, ticks=[-1, 0, 1], orientation='horizontal')
cbar.ax.set_xticklabels(['Low', 'Medium', 'High'])  # horizontal colorbar
```
