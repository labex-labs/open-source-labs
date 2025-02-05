# 绘制对角线

我们可以使用带有 `transform` 参数的 `axline` 来绘制具有固定斜率的对角线。让我们绘制斜率固定为 `0.5` 的对角网格线。

```python
import matplotlib.pyplot as plt
import numpy as np

# 绘制对角线
for pos in np.linspace(-2, 1, 10):
    plt.axline((pos, 0), slope=0.5, color='k', transform=plt.gca().transAxes)

plt.ylim([0, 1])
plt.xlim([0, 1])
plt.show()
```
