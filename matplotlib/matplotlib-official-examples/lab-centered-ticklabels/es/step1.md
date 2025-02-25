# Cargar los datos financieros

Primero, necesitamos cargar algunos datos financieros del precio de acciones de Google utilizando la función `cbook.get_sample_data()` de Matplotlib. Utilizaremos los últimos 250 días de datos.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Cargar algunos datos financieros; el precio de acciones de Google
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[-250:]  # obtener los últimos 250 días
```
