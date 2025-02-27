# Предсказание индексов цветов с использованием случайного кодбука

Мы будем предсказывать индексы цветов на полном изображении с использованием случайного кодбука.

```python
# Get a random codebook
codebook_random = shuffle(image_array, random_state=0, n_samples=n_colors)

# Predict color indices on the full image using the random codebook
print("Predicting color indices on the full image (random)")
t0 = time()
labels_random = pairwise_distances_argmin(codebook_random, image_array, axis=0)
print(f"done in {time() - t0:0.3f}s.")
```
