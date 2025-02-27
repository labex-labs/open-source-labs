# Cargar y Mostrar la Imagen Original

Comenzaremos cargando y mostrando la imagen original del Palacio de Verano.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_sample_image

# Cargar la foto del Palacio de Verano
china = load_sample_image("china.jpg")

# Mostrar la imagen original
plt.figure()
plt.axis("off")
plt.title("Imagen Original")
plt.imshow(china)
plt.show()
```
