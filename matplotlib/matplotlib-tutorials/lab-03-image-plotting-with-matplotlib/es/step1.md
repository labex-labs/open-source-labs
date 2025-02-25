# Importando datos de imágenes

Para comenzar, debemos importar las bibliotecas necesarias y cargar los datos de la imagen en una matriz de NumPy. En nuestro caso, usaremos la biblioteca `PIL` para cargar la imagen y luego la convertiremos en una matriz de NumPy.

```python
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open('./stinkbug.png'))
```
