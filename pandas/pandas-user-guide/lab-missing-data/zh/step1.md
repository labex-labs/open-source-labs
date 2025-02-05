# 导入必要的库并创建 DataFrame

首先，我们需要导入必要的库——pandas 和 NumPy。然后，我们将创建一个包含一些缺失值的 DataFrame。

```python
import pandas as pd
import numpy as np

# Create a DataFrame with missing values
df = pd.DataFrame(
   np.random.randn(5, 3),
   index=["a", "c", "e", "f", "h"],
   columns=["one", "two", "three"],
)
df["four"] = "bar"
df["five"] = df["one"] > 0
df2 = df.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])
```
