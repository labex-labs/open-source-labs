# 导入 Matplotlib 并创建散点图

我们首先导入 Matplotlib 并创建一个散点图。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sc = ax.scatter([1, 2], [1, 2], c=[1, 2])
```
