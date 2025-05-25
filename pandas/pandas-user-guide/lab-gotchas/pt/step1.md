# Compreendendo o Uso de Memória do DataFrame

O Pandas fornece vários métodos para entender o uso de memória de um DataFrame. O método `.info()` pode ser usado para ver um resumo, incluindo o uso de memória.

```python
import pandas as pd
import numpy as np

# Create a DataFrame
dtypes = ["int64", "float64", "datetime64[ns]", "timedelta64[ns]", "complex128", "object", "bool"]
n = 5000
data = {t: np.random.randint(100, size=n).astype(t) for t in dtypes}
df = pd.DataFrame(data)
df["categorical"] = df["object"].astype("category")

# Display DataFrame info
df.info()
```
