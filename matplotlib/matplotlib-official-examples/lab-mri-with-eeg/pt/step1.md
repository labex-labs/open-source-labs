# Carregar Dados de MRI e Exibir a Imagem

O primeiro passo é carregar os dados de MRI e exibir a imagem. Usaremos a função `imshow()` para exibir a imagem e `axis('off')` para remover os rótulos dos eixos.

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("MRI_with_EEG")

# Load the MRI data (256x256 16-bit integers)
im = np.load('mri_data.npy')

# Plot the MRI image
ax0 = fig.add_subplot(2, 2, 1)
ax0.imshow(im, cmap='gray')
ax0.axis('off')
```
