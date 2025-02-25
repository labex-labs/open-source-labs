# Das Verständnis der Speicherbenutzung von DataFrame

Pandas bietet mehrere Methoden, um die Speicherbenutzung eines DataFrame zu verstehen. Die `.info()`-Methode kann verwendet werden, um einen Überblick zu erhalten, einschließlich der Speicherbenutzung.

```python
import pandas as pd
import numpy as np

# Erstellen eines DataFrame
dtypes = ["int64", "float64", "datetime64[ns]", "timedelta64[ns]", "complex128", "object", "bool"]
n = 5000
data = {t: np.random.randint(100, size=n).astype(t) for t in dtypes}
df = pd.DataFrame(data)
df["categorical"] = df["object"].astype("category")

# Anzeige der DataFrame-Informationen
df.info()
```
