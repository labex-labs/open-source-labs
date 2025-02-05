# 生成随机数据

首先，我们需要生成 100 个随机数据集，每个数据集包含 1000 个介于 0 和 1 之间的随机数。我们将使用 numpy 的随机模块来生成随机数据。

```python
import numpy as np

np.random.seed(19680801)

X = np.random.rand(100, 1000)
```
