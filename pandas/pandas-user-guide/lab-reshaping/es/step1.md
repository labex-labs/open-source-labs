# Importando las bibliotecas necesarias y crear un DataFrame

Primero, importemos las bibliotecas necesarias y creemos un DataFrame para nuestros ejemplos.

```python
import pandas as pd
import numpy as np

# Crear DataFrame
np.random.seed([3, 1415])
n = 20
cols = np.array(["key", "row", "item", "col"])
df = cols + pd.DataFrame((np.random.randint(5, size=(n, 4)) // [2, 1, 2, 1]).astype(str))
df.columns = cols
df = df.join(pd.DataFrame(np.random.rand(n, 2).round(2)).add_prefix("val"))
```
