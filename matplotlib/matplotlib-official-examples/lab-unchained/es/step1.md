# Configuración

Antes de comenzar, debemos asegurarnos de que Matplotlib esté instalado. Puedes instalarlo utilizando pip, ejecutando el siguiente comando:

```python
!pip install matplotlib
```

Una vez instalado, debemos importar la biblioteca y configurar el entorno:

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# Create new Figure with black background
fig = plt.figure(figsize=(8, 8), facecolor='black')

# Add a subplot with no frame
ax = plt.subplot(frameon=False)
```
