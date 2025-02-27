# Charger et prétraiter l'image

Nous commencerons par charger l'image de monnaies grecques et la prétraiter pour la rendre plus facile à manipuler. Nous allons redimensionner l'image à 20% de sa taille d'origine et appliquer un filtre Gaussien pour le lissage avant la réduction d'échelle pour réduire les artefacts d'aliasing.

```python
# charger les monnaies sous forme d'un tableau numpy
orig_coins = coins()

# Redimensionnez-la à 20% de sa taille d'origine pour accélérer le traitement
# Appliquer un filtre Gaussien pour le lissage avant la réduction d'échelle
# réduit les artefacts d'aliasing.
smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(smoothened_coins, 0.2, mode="reflect", anti_aliasing=False)
```
