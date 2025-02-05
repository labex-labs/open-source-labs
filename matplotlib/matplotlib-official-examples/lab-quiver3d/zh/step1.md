# 导入库并设置绘图

第一步是导入必要的库并设置绘图。在本示例中，我们将使用 Matplotlib 的 `pyplot` 模块及其 `3d` 工具包来创建三维绘图。

```python
import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')
```
