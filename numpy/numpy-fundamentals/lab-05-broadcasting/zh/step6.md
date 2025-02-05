# 实际示例 - 矢量量化

让我们探讨一个广播很有用的实际示例。考虑信息论和分类中使用的矢量量化（VQ）算法。VQ 中的基本操作是在一组点中找到与给定点最接近的点。这可以通过广播来完成。以下是一个示例：

```python
import numpy as np

observation = np.array([111.0, 188.0])
codes = np.array([[102.0, 203.0],
                  [132.0, 193.0],
                  [45.0, 155.0],
                  [57.0, 173.0]])
diff = codes - observation
dist = np.sqrt(np.sum(diff**2, axis=-1))
closest_index = np.argmin(dist)
closest_code = codes[closest_index]
```

在这个示例中，`observation` 表示要分类的运动员的体重和身高，`codes` 表示不同类别的运动员。通过从 `codes` 中减去 `observation`，使用广播来计算 `observation` 与每个代码之间的距离。然后使用 `argmin` 函数找到最接近代码的索引。
