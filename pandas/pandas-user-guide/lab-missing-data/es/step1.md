# Importar las bibliotecas necesarias y crear un DataFrame

Para comenzar, necesitamos importar las bibliotecas necesarias: pandas y NumPy. Luego, crearemos un DataFrame con algunos valores faltantes.

```python
import pandas as pd
import numpy as np

# Crear un DataFrame con valores faltantes
df = pd.DataFrame(
   np.random.randn(5, 3),
   index=["a", "c", "e", "f", "h"],
   columns=["one", "two", "three"],
)
df["four"] = "bar"
df["five"] = df["one"] > 0
df2 = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
```
