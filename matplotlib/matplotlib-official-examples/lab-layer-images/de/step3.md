# Definiere die Ausdehnung und erstelle das erste Bild

Definiere die Ausdehnung und erstelle das erste Bild mit der `imshow`-Funktion.

```python
extent = np.min(x), np.max(x), np.min(y), np.max(y)
Z1 = np.add.outer(range(8), range(8)) % 2  # Schachbrett
im1 = plt.imshow(Z1, cmap=plt.cm.gray, interpolation='nearest',
                 extent=extent)
```
