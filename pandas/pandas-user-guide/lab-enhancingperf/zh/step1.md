# 设置并创建示例数据

在开始之前，让我们导入必要的模块并创建一个示例 DataFrame。

```python
# 导入必要的模块
import pandas as pd
import numpy as np

# 创建一个示例 DataFrame
df = pd.DataFrame(
    {
        "a": np.random.randn(1000),
        "b": np.random.randn(1000),
        "N": np.random.randint(100, 1000, (1000)),
        "x": "x",
    }
)
df
```
