# 检查数据类型

第一步是检查 x 轴值的数据类型。如果它是一个字符串列表，那么刻度行为很可能不符合预期。要解决这个问题，我们需要将字符串转换为数值类型。以下是一个示例：

```python
import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# 绘制带有字符串刻度标签的数据
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Categories')
plt.show()
```

在这个示例中，x 轴上有一个字符串列表。当我们绘制数据时，刻度标签顺序混乱且位置错误。
