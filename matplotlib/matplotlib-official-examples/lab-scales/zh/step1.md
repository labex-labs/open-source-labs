# 导入库并生成数据

首先，我们需要导入必要的库并生成一些要绘制的数据。在这个例子中，我们将使用正态分布来生成 y 轴的数据。

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))
```
