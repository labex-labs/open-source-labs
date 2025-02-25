# Charger les données IRM et afficher l'image

La première étape consiste à charger les données IRM et à afficher l'image. Nous utiliserons la fonction `imshow()` pour afficher l'image et `axis('off')` pour supprimer les étiquettes d'axe.

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("MRI_with_EEG")

# Charger les données IRM (entiers signés 16 bits, 256x256)
im = np.load('mri_data.npy')

# Tracer l'image IRM
ax0 = fig.add_subplot(2, 2, 1)
ax0.imshow(im, cmap='gray')
ax0.axis('off')
```
