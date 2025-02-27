# Bild laden und vorverarbeiten

Wir beginnen mit dem Laden des Bildes griechischer Münzen und dessen Vorverarbeitung, um es einfacher zu bearbeiten. Wir verkleinern das Bild auf 20 % seiner ursprünglichen Größe und wenden einen Gauß-Filter zur Glättung an, bevor wir es verkleinern, um Aliasing-Artifakte zu reduzieren.

```python
# ladet die Münzen als numpy-Array
orig_coins = coins()

# Verkleinert es auf 20 % seiner ursprünglichen Größe, um die Verarbeitung zu beschleunigen
# Wenden Sie einen Gauß-Filter zur Glättung an, bevor Sie es verkleinern
# reduziert Aliasing-Artifakte.
smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(smoothened_coins, 0.2, mode="reflect", anti_aliasing=False)
```
