# Crear datos de prueba

Primero, crearemos algunos datos de prueba para utilizar en el diagrama de violín. Utilizaremos NumPy para generar cuatro matrices de 100 valores distribuidos normalmente con desviaciones estándar crecientes.

```python
import matplotlib.pyplot as plt
import numpy as np

# create test data
np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
```
