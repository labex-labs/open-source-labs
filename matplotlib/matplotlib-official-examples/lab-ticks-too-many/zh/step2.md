# 将字符串转换为数值类型

为了修正刻度行为，我们需要将字符串转换为数值类型。以下是一个示例：

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# 将字符串转换为浮点数
x = np.asarray(x, dtype='float')

# 绘制带有数字刻度标签的数据
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Floats')
plt.show()
```

在这个示例中，我们使用 `np.asarray()` 将字符串值转换为浮点数。当我们再次绘制数据时，刻度标签就符合预期了。
