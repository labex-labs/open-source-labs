# Ergebnisse visualisieren

Wir werden das ursprüngliche Bild und das segmentierte Bild nebeneinander mit Hilfe von `matshow` aus `matplotlib.pyplot` plotten.

```python
import matplotlib.pyplot as plt

label_im = np.full(mask.shape, -1.0)
label_im[mask] = labels

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axs[0].matshow(img)
axs[1].matshow(label_im)

plt.show()
```
