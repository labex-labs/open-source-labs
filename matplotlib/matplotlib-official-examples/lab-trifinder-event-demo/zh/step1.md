# 创建三角剖分对象

首先，我们需要创建一个三角剖分对象。我们将使用 `matplotlib.tri` 中的 `Triangulation` 类。在这个例子中，我们将用随机数据创建一个三角剖分对象。

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation

# 生成随机数据
x = np.random.rand(10)
y = np.random.rand(10)
triang = Triangulation(x, y)
```
