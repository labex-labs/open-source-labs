# 了解 DataFrame 的内存使用情况

Pandas 提供了多种方法来了解 DataFrame 的内存使用情况。`.info()` 方法可用于查看摘要，包括内存使用情况。

```python
import pandas as pd
import numpy as np

# 创建一个 DataFrame
dtypes = ["int64", "float64", "datetime64[ns]", "timedelta64[ns]", "complex128", "object", "bool"]
n = 5000
data = {t: np.random.randint(100, size=n).astype(t) for t in dtypes}
df = pd.DataFrame(data)
df["categorical"] = df["object"].astype("category")

# 显示 DataFrame 信息
df.info()
```
