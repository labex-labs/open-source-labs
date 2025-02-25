# Загрузка данных МРТ и отображение изображения

Первым шагом является загрузка данных МРТ и отображение изображения. Мы будем использовать функцию `imshow()` для отображения изображения и `axis('off')` для удаления подписей осей.

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
