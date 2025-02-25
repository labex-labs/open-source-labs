# Importar las bibliotecas y datos necesarios

En primer lugar, necesitamos importar las bibliotecas necesarias, que son `matplotlib`, `numpy` y `matplotlib.cbook`. También necesitamos cargar una matriz de registros de numpy a partir de datos csv de yahoo con los campos fecha, apertura, alta, baja, cierre, volumen, cierre ajustado desde el directorio mpl-data/sample_data. La matriz de registros almacena la fecha como un np.datetime64 con una unidad de día ('D') en la columna de fecha. Utilizaremos estos datos para trazar la serie temporal financiera.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Cargar datos desde el directorio sample_data
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[:9]  # obtener los primeros 9 días
```
