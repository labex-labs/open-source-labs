# Понимание использования памяти DataFrame

Pandas предоставляет несколько методов для понимания использования памяти DataFrame. Метод `.info()` можно использовать, чтобы увидеть сводку, включая использование памяти.

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
