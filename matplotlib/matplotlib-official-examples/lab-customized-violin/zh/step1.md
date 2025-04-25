# 创建测试数据

首先，我们将创建一些用于小提琴图的测试数据。我们将使用 NumPy 生成四个包含 100 个正态分布值的数组，其标准差逐渐增加。

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建测试数据
np.random.seed(19680801)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
```
