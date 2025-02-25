# Construyendo arrays de enteros anulables

Pandas proporciona la clase `IntegerArray` para crear arrays de enteros anulables. Comencemos creando un `IntegerArray`.

```python
# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np

# Crear un IntegerArray con valores faltantes
arr = pd.array([1, 2, None], dtype=pd.Int64Dtype())
# Salida: <IntegerArray>
# [1, 2, <NA>]
# Longitud: 3, tipo de datos: Int64
```

También puede usar el alias de cadena "Int64" para especificar el tipo de datos al crear el array. Todos los valores similares a NA se reemplazan con `pandas.NA`.

```python
# Crear un IntegerArray usando el alias de cadena "Int64"
arr = pd.array([1, 2, np.nan], dtype="Int64")
# Salida: <IntegerArray>
# [1, 2, <NA>]
# Longitud: 3, tipo de datos: Int64
```
