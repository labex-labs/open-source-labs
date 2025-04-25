# 创建可空整数数组

Pandas 提供了`IntegerArray`类来创建可空整数数组。让我们从创建一个`IntegerArray`开始。

```python
# 导入必要的库
import pandas as pd
import numpy as np

# 创建一个包含缺失值的 IntegerArray
arr = pd.array([1, 2, None], dtype=pd.Int64Dtype())
# 输出：<IntegerArray>
# [1, 2, <NA>]
# 长度：3, 数据类型：Int64
```

在创建数组时，你也可以使用字符串别名“Int64”来指定数据类型。所有类似 NA 的值都会被替换为`pandas.NA`。

```python
# 使用“Int64”字符串别名创建一个 IntegerArray
arr = pd.array([1, 2, np.nan], dtype="Int64")
# 输出：<IntegerArray>
# [1, 2, <NA>]
# 长度：3, 数据类型：Int64
```
