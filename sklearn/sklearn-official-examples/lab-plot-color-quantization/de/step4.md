# Farb-Indizes mit einem zufälligen Codebuch vorhersagen

Wir werden die Farb-Indizes für das gesamte Bild mit einem zufälligen Codebuch vorherzusagen.

```python
# Holt ein zufälliges Codebuch
codebook_random = shuffle(image_array, random_state=0, n_samples=n_colors)

# Vorhersagt die Farb-Indizes für das gesamte Bild mit dem zufälligen Codebuch
print("Vorhersagen von Farb-Indizes für das gesamte Bild (zufällig)")
t0 = time()
labels_random = pairwise_distances_argmin(codebook_random, image_array, axis=0)
print(f"fertig in {time() - t0:0.3f}s.")
```
