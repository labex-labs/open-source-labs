# Predecir Índices de Color Utilizando un Código Aleatorio

Predeciremos los índices de color en la imagen completa utilizando un código aleatorio.

```python
# Obtener un código aleatorio
codebook_random = shuffle(image_array, random_state=0, n_samples=n_colors)

# Predecir índices de color en la imagen completa utilizando el código aleatorio
print("Predecir índices de color en la imagen completa (aleatorio)")
t0 = time()
labels_random = pairwise_distances_argmin(codebook_random, image_array, axis=0)
print(f"hecho en {time() - t0:0.3f}s.")
```
