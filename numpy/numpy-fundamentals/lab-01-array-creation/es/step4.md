# Leer arrays desde el disco

Puedes leer arrays desde el disco en varios formatos. Para formatos binarios estándar, hay bibliotecas de Python como h5py para HDF5 y Astropy para FITS. Para formatos ASCII comunes como CSV y TSV, puedes utilizar las funciones `np.loadtxt` y `np.genfromtxt`. Aquí hay un ejemplo de lectura de un archivo CSV:

```python
import numpy as np

data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
```
