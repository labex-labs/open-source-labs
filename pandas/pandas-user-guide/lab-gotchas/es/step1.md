# Comprendiendo el uso de memoria de DataFrame

Pandas proporciona varios métodos para comprender el uso de memoria de un DataFrame. El método `.info()` se puede utilizar para ver un resumen, incluyendo el uso de memoria.

```python
import pandas as pd
import numpy as np

# Crea un DataFrame
dtypes = ["int64", "float64", "datetime64[ns]", "timedelta64[ns]", "complex128", "object", "bool"]
n = 5000
data = {t: np.random.randint(100, size=n).astype(t) for t in dtypes}
df = pd.DataFrame(data)
df["categorical"] = df["object"].astype("category")

# Muestra la información del DataFrame
df.info()
```
