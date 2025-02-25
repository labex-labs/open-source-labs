# Importieren von erforderlichen Bibliotheken und Erstellen eines DataFrames

Zunächst müssen wir die erforderlichen Bibliotheken importieren - pandas und NumPy. Anschließend erstellen wir einen DataFrame mit einigen fehlenden Werten.

```python
import pandas as pd
import numpy as np

# Erstellen eines DataFrames mit fehlenden Werten
df = pd.DataFrame(
   np.random.randn(5, 3),
   index=["a", "c", "e", "f", "h"],
   columns=["one", "two", "three"],
)
df["four"] = "bar"
df["five"] = df["one"] > 0
df2 = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
```
