# Sobreescribir el comportamiento de las ufunc

Las clases, incluyendo las subclases de ndarray, pueden sobrescribir cómo las ufunc actúan sobre ellas definiendo ciertos métodos especiales. Esto permite la personalización del comportamiento de las ufunc. Echemos un ejemplo.

```python
import numpy as np

# Define una clase personalizada
class MyArray(np.ndarray):
    def __add__(self, other):
        print("Custom add method called")
        return super().__add__(other)

# Crea una instancia de la clase personalizada
arr = MyArray([1, 2, 3])

# Realiza una adición
result = arr + 1

# Imprime el resultado
print(result)
```

Salida:

```
Custom add method called
[2 3 4]
```
