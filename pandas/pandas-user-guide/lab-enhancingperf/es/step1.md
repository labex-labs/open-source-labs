# Configuración y creación de datos de muestra

Antes de comenzar, importemos los módulos necesarios y creemos un DataFrame de muestra.

```python
# Import necessary modules
import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.DataFrame(
    {
        "a": np.random.randn(1000),
        "b": np.random.randn(1000),
        "N": np.random.randint(100, 1000, (1000)),
        "x": "x",
    }
)
df
```
