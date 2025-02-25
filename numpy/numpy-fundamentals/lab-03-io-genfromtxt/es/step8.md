# Usando funciones de atajo

El módulo `numpy.lib.npyio` proporciona funciones de atajo derivadas de `numpy.genfromtxt`. Estas funciones tienen valores predeterminados diferentes y devuelven una matriz estándar de NumPy o una matriz enmascarada.

```python
from numpy.lib.npyio import recfromtxt

recfromtxt(StringIO(data), delimitador=",")
```
