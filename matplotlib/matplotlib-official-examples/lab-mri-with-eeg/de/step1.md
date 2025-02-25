# MRT-Daten laden und das Bild anzeigen

Der erste Schritt besteht darin, die MRT-Daten zu laden und das Bild anzuzeigen. Wir werden die `imshow()`-Funktion verwenden, um das Bild anzuzeigen, und `axis('off')`, um die Achsenbeschriftungen zu entfernen.

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("MRI_with_EEG")

# Lade die MRT-Daten (256x256 16-Bit-Ganzzahlen)
im = np.load('mri_data.npy')

# Plotte das MRT-Bild
ax0 = fig.add_subplot(2, 2, 1)
ax0.imshow(im, cmap='gray')
ax0.axis('off')
```
