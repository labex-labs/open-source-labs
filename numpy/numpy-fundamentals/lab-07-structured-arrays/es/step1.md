# Creación de un array estructurado

Para crear un array estructurado, podemos utilizar la función `np.array` y especificar el tipo de datos utilizando el parámetro `dtype`. El tipo de datos debe ser una lista de tuplas, donde cada tupla representa un campo en el array estructurado. Cada tupla debe contener el nombre del campo y el tipo de datos del campo.

```python
import numpy as np

# Crea un array estructurado
x = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
