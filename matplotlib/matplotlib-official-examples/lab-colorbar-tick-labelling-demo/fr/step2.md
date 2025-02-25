# Créez un graphique avec une barre de couleur verticale

Nous commencerons par créer un graphique avec une barre de couleur verticale. Nous allons générer des données aléatoires en utilisant `randn` de `numpy` et limiter les valeurs à la plage de -1 à 1. Nous créerons ensuite un objet `AxesImage` en utilisant `imshow` et la carte de couleur `coolwarm`. Enfin, nous ajouterons un titre au graphique.

```python
# Make plot with vertical (default) colorbar
fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.coolwarm)
ax.set_title('Gaussian noise with vertical colorbar')
```
