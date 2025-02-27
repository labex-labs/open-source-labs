# Bild in Floats umwandeln und umformen

Wir werden das Bild in Floats umwandeln und es in ein 2D-Numpy-Array umformen, damit es vom K-Means-Algorithmus verarbeitet werden kann.

```python
# Konvertiere zu Floats anstelle der standardmäßigen 8-Bit-Ganzzahl-Codierung.
china = np.array(china, dtype=np.float64) / 255

# Ermittle die Dimensionen des Bilds
w, h, d = original_shape = tuple(china.shape)
assert d == 3

# Forme das Bild in ein 2D-Numpy-Array um
image_array = np.reshape(china, (w * h, d))
```
