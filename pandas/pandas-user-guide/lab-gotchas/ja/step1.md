# DataFrame のメモリ使用量を理解する

Pandas は、DataFrame のメモリ使用量を理解するためのいくつかのメソッドを提供しています。`.info()` メソッドを使うと、メモリ使用量を含む要約を表示できます。

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
