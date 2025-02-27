# Generar datos

Comenzaremos generando los datos. Usaremos el conjunto de datos `coins` de scikit-image, que es una imagen en escala de grises bidimensional de monedas. Redimensionaremos la imagen al 20% de su tamaño original para acelerar el procesamiento.

```python
from skimage.data import coins
import numpy as np
from scipy.ndimage import gaussian_filter
from skimage.transform import rescale

orig_coins = coins()

# Redimensionarla al 20% de su tamaño original para acelerar el procesamiento
# Aplicar un filtro Gaussiano para suavizar antes de la reducción de escala
# reduce los artefactos de aliasing.

smoothened_coins = gaussian_filter(orig_coins, sigma=2)
rescaled_coins = rescale(
    smoothened_coins,
    0.2,
    mode="reflect",
    anti_aliasing=False,
)

X = np.reshape(rescaled_coins, (-1, 1))
```
