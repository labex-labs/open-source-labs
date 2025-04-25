# 创建稀疏数组

首先，我们创建一个稀疏数组，它是一种 pandas 数据结构，用于高效存储稀疏值数组。稀疏值是那些由于与大多数值相似而未被存储的值，因此被视为冗余值。

```python
# 导入必要的库
import pandas as pd
import numpy as np

# 创建一个具有随机值的 numpy 数组
arr = np.random.randn(10)

# 将一些值设置为 NaN
arr[2:-2] = np.nan

# 使用 pandas 创建一个稀疏数组
ts = pd.Series(pd.arrays.SparseArray(arr))

# 输出稀疏数组
print(ts)
```
