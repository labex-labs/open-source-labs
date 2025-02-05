# 导入必要的库并创建 DataFrame

首先，让我们导入必要的库，并为我们的示例创建一个 DataFrame。

```python
import pandas as pd
import numpy as np

# 创建 DataFrame
np.random.seed([3, 1415])
n = 20
cols = np.array(["key", "row", "item", "col"])
df = cols + pd.DataFrame((np.random.randint(5, size=(n, 4)) // [2, 1, 2, 1]).astype(str))
df.columns = cols
df = df.join(pd.DataFrame(np.random.rand(n, 2).round(2)).add_prefix("val"))
```
