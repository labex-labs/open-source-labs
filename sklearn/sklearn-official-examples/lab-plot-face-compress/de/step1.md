# Originalbild laden und anzeigen

Wir beginnen mit dem Laden des Waschbärenbildes aus Scipy. Wir werden das Bild anzeigen und seine Form, den Datentyp und den Arbeitsspeicherbedarf überprüfen.

```python
from scipy.misc import face
import matplotlib.pyplot as plt

raccoon_face = face(gray=True)

print(f"Die Dimension des Bildes ist {raccoon_face.shape}")
print(f"Die Daten, die zum Codieren des Bildes verwendet werden, sind vom Typ {raccoon_face.dtype}")
print(f"Die Anzahl der in RAM verwendeten Bytes beträgt {raccoon_face.nbytes}")

fig, ax = plt.subplots(ncols=2, figsize=(12, 4))
ax[0].imshow(raccoon_face, cmap=plt.cm.gray)
ax[0].axis("off")
ax[0].set_title("Originalbild")
ax[1].hist(raccoon_face.ravel(), bins=256)
ax[1].set_xlabel("Pixelwert")
ax[1].set_ylabel("Anzahl der Pixel")
ax[1].set_title("Verteilung der Pixelwerte")
_ = fig.suptitle("Originalbild eines Waschbärenengesichts")
```
