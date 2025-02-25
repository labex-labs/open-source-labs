# Importieren von erforderlichen Bibliotheken und Erstellen eines DataFrames

Zunächst importieren wir die erforderlichen Bibliotheken und erstellen einen DataFrame für unsere Beispiele.

```python
import pandas as pd
import numpy as np

# Create DataFrame
np.random.seed([3, 1415])
n = 20
cols = np.array(["key", "row", "item", "col"])
df = cols + pd.DataFrame((np.random.randint(5, size=(n, 4)) // [2, 1, 2, 1]).astype(str))
df.columns = cols
df = df.join(pd.DataFrame(np.random.rand(n, 2).round(2)).add_prefix("val"))
```
