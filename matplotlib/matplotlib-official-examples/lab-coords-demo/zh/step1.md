# 创建正弦波图

首先，我们需要使用 numpy 和 matplotlib 库创建一个正弦波图。

```python
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)
```
