# Reglas de conversión de tipos

La conversión de tipos se realiza en las entradas de una ufunc cuando no hay una implementación de bucle principal para los tipos de entrada proporcionados. Las reglas de conversión determinan cuándo un tipo de datos se puede convertir con seguridad a otro tipo de datos. Echemos un ejemplo.

```python
import numpy as np

# Comprueba si int se puede convertir con seguridad a float
result = np.can_cast(np.int, np.float)

# Imprime el resultado
print(result)
```

Salida:

```
True
```
