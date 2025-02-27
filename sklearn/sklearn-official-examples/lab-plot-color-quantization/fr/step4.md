# Prédire les indices de couleur à l'aide d'un livre de codes aléatoire

Nous allons prédire les indices de couleur sur l'image complète à l'aide d'un livre de codes aléatoire.

```python
# Obtenir un livre de codes aléatoire
codebook_random = shuffle(image_array, random_state=0, n_samples=n_colors)

# Prédire les indices de couleur sur l'image complète à l'aide du livre de codes aléatoire
print("Prédiction des indices de couleur sur l'image complète (aléatoire)")
t0 = time()
labels_random = pairwise_distances_argmin(codebook_random, image_array, axis=0)
print(f"terminé en {time() - t0:0.3f}s.")
```
