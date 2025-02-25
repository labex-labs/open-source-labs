# Cargar datos de resonancia magnética y mostrar la imagen

El primer paso es cargar los datos de resonancia magnética y mostrar la imagen. Utilizaremos la función `imshow()` para mostrar la imagen y `axis('off')` para eliminar las etiquetas de los ejes.

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("MRI_with_EEG")

# Cargar los datos de resonancia magnética (enteros de 16 bits de 256x256)
im = np.load('mri_data.npy')

# Graficar la imagen de resonancia magnética
ax0 = fig.add_subplot(2, 2, 1)
ax0.imshow(im, cmap='gray')
ax0.axis('off')
```
